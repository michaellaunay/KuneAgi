ssh wholphin
sudo -i
cd /home/dokku/kuneagi/.volumes/
tar zcvf /tmp/kuneagi.tar.gz var/blobstorage var/filestorage/
exit
exit

cd workspace/kuneagi
scp wholphin:/tmp/kuneagi.tar.gz .
tar xvf kuneagi.tar.gz
./run.sh rebuild
./run.sh
docker exec -it kuneagi_novaideo_1 /app/bin/pshell /app/production-heroku.ini

>>> root['principals']['users']['Sergio-Arbarviro'].set_password('000000')
>>> root['principals']['users']['Sergio-Arbarviro'].email
'sergio.arbarviro@kuneagi.org'
>>> import transaction
>>> transaction.commit()
