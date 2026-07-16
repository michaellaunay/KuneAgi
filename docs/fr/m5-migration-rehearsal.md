# M5 — répétition de migration de données (mode opératoire)

*Phase 3, jalon final. English version: [`../en/m5-migration-rehearsal.md`](../en/m5-migration-rehearsal.md).*

La répétition fait traverser la pile moderne à une **copie d'une vraie
base de production** : extraction → vérification → recensement → boot
(sans réacteur) → evolve → requêtes → réindexation → pack → balayage
final. Première exécution le 16/07/2026 sur une instance KuneAgi de
Cosmopolitical ; les résultats mesurés sont en bas de page.

## Règles de confidentialité (non négociables)

Une copie de production contient de vrais membres : noms, **adresses
mail à jour**, hachés d'identifiants, jetons d'invitation. En
conséquence :

- travailler sur des copies, sur des machines éphémères ; supprimer à
  la fin ;
- agrégats uniquement dans toute sortie, log, fil de l'eau et
  livrable — comptes, noms de classes, identifiants d'étapes ; jamais
  une clé, un titre, un login ou une adresse
  (``tools/m5_rehearsal.py`` est construit ainsi) ;
- **ne jamais démarrer l'application avec le réacteur sur ces
  données** : dix ans de timers expirés se réarmeraient et se
  déclencheraient — des behaviors s'exécuteraient, et des alertes
  écriraient à des adresses *actuelles*. L'outil inclut
  ``dace.wosystem`` (scan + étapes d'évolution, pas de réacteur) et
  remplace le mailer par un ``DummyMailer`` avant toute ouverture.

## 1. Extraction côté serveur

Sur l'hôte de production (le pack préalable vaut la peine — cette
instance est passée de 472 Mo à 15 Mo) :

```bash
bin/zeopack -u ./var/zeo.sock -d 0          # ZEO vivant, sans coupure
docker cp tools/decrypt_copy.py <conteneur>:/app/
docker exec -w /app <conteneur> bin/py decrypt_copy.py
tar cf kuneagi-plain-$(date +%Y%m%d).tar var/filestorage/Data-plain2.fs
```

Pourquoi ``decrypt_copy.py`` procède ainsi — deux leçons payées :

- **les transform storages déchiffrent sur ``load()``, pas à
  l'itération** : l'itérateur de réplication (celui de
  ``copyTransactionsFrom``) sert les octets au repos tels quels — une
  copie naïve par client ZEO reste chiffrée ;
- le ``cipher.encryptingstorage`` d'époque est un checkout source
  patché dont le constructeur diffère de la release moderne : l'outil
  laisse **ZConfig assembler la pile exactement comme ``zeo.conf``**
  (même ``%import``, même section, même ``etc/encryption.conf``) — les
  clés ne quittent jamais le serveur.

La sortie préserve oids et serials : le ``var/blobstorage`` d'origine,
jamais chiffré, s'apparie tel quel. L'historique d'undo ne voyage pas
(états courants seuls) : la copie arrive pré-compactée.

## 2. La répétition

Dans le harnais moderne (`tools/bootstrap-modern.sh`) :

```bash
.venv312/bin/python tools/m5_rehearsal.py \
    --data work/Data-plain.fs --blobs work/blobstorage
```

Phases et échecs durs : enregistrements encore transformés (code 2),
tout objet broken ou inchargeable (code 3), index reconstruits en
désaccord avec les index d'époque (code 4), comptes instables
(code 5). Le code 0 imprime ``REHEARSAL PASSED``.

## 3. Résultats mesurés (16/07/2026, première exécution)

| Contrôle | Résultat |
|---|---|
| Déchiffrement | 79 269 enregistrements, 100 % en clair après extraction |
| Balayage intégral | **381 classes, 0 broken, 0 inchargeable** |
| Étapes d'évolution | 73 finies dans la base ; **0 non finie** sur le code moderne — la chaîne est un no-op |
| Boot applicatif | le vrai ``novaideo.main`` se configure sur les données de production (sans réacteur) |
| Requêtes sur index d'époque | comptes idées/propositions/personnes servis par hypatia 0.5 |
| Réindexation intégrale | 61 index reconstruits sur 3 catalogues ; **comptes de requêtes identiques** avant/après |
| Pack | passe ; gain marginal (la copie arrive compactée) |
| Balayage final | comptes stables (utilisateurs, processus, définitions) |

Dix ans de pickles se désérialisent sans faute sur Python 3.12 /
ZODB 6 — état persistant du moteur compris (``Transaction``, ``Path``,
``WorkItem``, ``Activity``). C'est la règle du jamais-bouger des
classes persistantes que ce jalon encaisse.

## 4. Constats pour le côté production

Indépendamment de la migration : le recensement au repos a montré
**64 987 enregistrements chiffrés contre 14 282 en clair** — la
configuration de chiffrement a dérivé à une période — et les blobs
(pièces jointes, avatars) ne sont jamais chiffrés par ce wrapper. Un
audit de la configuration de chiffrement de la production est
recommandé.
