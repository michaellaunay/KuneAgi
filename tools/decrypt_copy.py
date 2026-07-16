# decrypt_copy_v3.py — run INSIDE the container, from /app:
#
#     docker cp decrypt_copy_v3.py <container>:/app/
#     docker exec -w /app <container> bin/py decrypt_copy_v3.py
#
# v3: the era cipher.encryptingstorage (a patched source checkout) has
# a different constructor signature than the modern release — so we
# stop guessing and let ZConfig assemble the storage stack EXACTLY as
# zeo.conf does in production (same %import, same section, same
# encryption config). load() through that stack is the application's
# own decrypting path.
#
# Afterwards:
#     tar cf kuneagi-plain2-$(date +%Y%m%d).tar var/filestorage/Data-plain2.fs
#
import shutil

import ZODB.config
from ZODB.FileStorage import FileStorage
from ZODB.Connection import TransactionMetaData

SRC_COPY = '/tmp/Data-src.fs'
DST_PATH = 'var/filestorage/Data-plain2.fs'

print('copying the live Data.fs (crash-consistent) ...')
shutil.copyfile('var/filestorage/Data.fs', SRC_COPY)

src = ZODB.config.storageFromString('''
%%import cipher.encryptingstorage

<encryptingstorage>
  config etc/encryption.conf
  <filestorage>
    path %s
    read-only true
  </filestorage>
</encryptingstorage>
''' % SRC_COPY)

print('pass 1: current serial of every oid ...')
current = {}
for txn in src.iterator():          # raw is fine: only oids/tids used
    for rec in txn:
        if rec.data is None:
            current.pop(rec.oid, None)
        else:
            current[rec.oid] = rec.tid
print('  %d live objects' % len(current))

groups = {}
for oid, tid in current.items():
    groups.setdefault(tid, []).append(oid)

dst = FileStorage(DST_PATH)
print('pass 2: decrypt-load and restore, %d transactions ...'
      % len(groups))
done = 0
for tid in sorted(groups):
    txn = TransactionMetaData()
    dst.tpc_begin(txn, tid=tid)
    for oid in groups[tid]:
        data, _ = src.load(oid, '')     # decrypted by the stack
        dst.restore(oid, tid, data, '', None, txn)
        done += 1
    dst.tpc_vote(txn)
    dst.tpc_finish(txn)
print('  %d objects restored' % done)

dst.close()
src.close()
print('done:', DST_PATH,
      '(pairs with the original var/blobstorage — same oids/serials)')
