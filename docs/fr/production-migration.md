# Migration de production — runbook (pile moderne)

*Compagnon de la phase 3. Prérequis : la répétition de migration sur
copie réelle de production doit être PASSÉE — voir
[`m5-migration-rehearsal.md`](m5-migration-rehearsal.md). Version
anglaise : [`../en/production-migration.md`](../en/production-migration.md).*

Les artefacts d'appui référencés ici sont dans le dépôt :
[`etc/production-modern.ini.example`](../../etc/production-modern.ini.example)
(gabarit de configuration cible, profil de réveil inclus) et
`novaideo/utilities/dummy_sms.py` (le puits SMS).

## 0. Principes

- **L'instance source n'est jamais modifiée.** Chaque étape lit une
  copie ; le conteneur legacy continue de tourner jusqu'à la bascule
  finale, et reste le rollback jusqu'à sa mise hors service.
- **Le réacteur ne se réveille que contre des puits.** Dix ans de
  timers expirés VONT partir au premier boot : le profil de réveil
  écrit les mails sur disque et retient les SMS. Ne jamais booter une
  base migrée sur un profil mail réel en premier.
- **Observation en agrégats seulement** (comptes, états) : les données
  de production restent hors des terminaux, tickets et conversations.

## 1. Geler et extraire

1. Annoncer la fenêtre de maintenance ; arrêter les processus
   applicatifs legacy (ZEO peut rester pour l'extraction).
2. Ceinture et bretelles : sauvegarde `repozo` du `Data.fs` vivant.
3. Packer, puis copier `Data.fs` et `blobstorage/` vers l'hôte cible.
4. **Base chiffrée** (`cipher.encryptingstorage`) : produire la copie
   claire avec `tools/decrypt_copy.py` en client ZEO lecture seule sur
   la socket vivante — les clés ne quittent jamais l'hôte source.
   Procédure et pièges : voir le runbook de répétition.

## 2. Construire la cible

1. Cloner le quatuor côte à côte et amorcer :

   ```bash
   git clone git@github.com:michaellaunay/dace.git
   git clone git@github.com:michaellaunay/pontus.git
   git clone git@github.com:michaellaunay/daceui.git
   git clone git@github.com:michaellaunay/KuneAgi.git
   cd KuneAgi && tools/bootstrap-modern.sh
   ```

   **Épingler la cible.** Consigner les quatre shas de commit au
   journal de migration — la construction n'est une cible valide que
   si les deux étages de CI sont verts à ces commits ET si la suite de
   caractérisation complète (128 tests) passe localement sur la
   construction fraîche, en ses deux moitiés (les filtres `-m` exacts
   sont dans [`modern-harness.md`](modern-harness.md)). Cela prouve la
   cible AVANT toute donnée de production. Après le merge-back vers
   l'organisation `ecreall`, substituer les URLs `ecreall/...` — les
   histoires avancent en fast-forward, les arbres sont identiques.

2. `cp etc/production-modern.ini.example etc/production.ini`, puis
   éditer : secrets, URL publique, `mail.default_sender`, langues.
   Garder `tm.annotate_user = false` (non optionnel sur la pile
   moderne) et garder pour l'instant le **bloc du profil de réveil**
   tel que livré (`pyramid_mailer.debug` → `var/mail-out/`,
   `sms.service` → `DummySMSService`).

## 3. Poser les données

Placer le `Data.fs` extrait (clair) sous `var/filestorage/` et les
blobs sous `var/blobstorage/` ; créer `var/mail-out/` et
`var/tmp_uploads/` ; vérifier propriétaire et permissions.

## 4. Réveil contrôlé

1. Premier boot sur le profil de réveil. Attendre le drainage des
   timers expirés par le réacteur : surveiller les logs et le
   **compte** des fichiers arrivant dans `var/mail-out/` (ne pas lire
   les corps), et les lignes de rétention du `DummySMSService`.
2. Dérouler les étapes d'évolution (équivalent `sdi evolve`) ; la
   répétition a montré une chaîne NO-OP sur cette base — tout autre
   résultat est un signal d'arrêt.
3. Optionnel : réindexation complète ; la référence de répétition est
   *comptes identiques sur les 61 index*.
4. Laisser l'instance atteindre la quiescence (mail-out cesse de
   croître).

## 5. Portes de vérification

- L'application boote et sert ; le login admin fonctionne — cette
  porte prouve aussi que les hachés de mots de passe D'ÉPOQUE
  (`$2a`, cryptacular) se vérifient sous la pile moderne : le
  correctif d'API mot de passe de la campagne honore les deux
  générations (compatibles bcrypt).
- Le recensement en agrégats colle aux chiffres de répétition pour
  cette base (enregistrements, classes, zéro broken).
- Les requêtes de catalogue répondent ; les listes clés se rendent.
- Le volume de `var/mail-out/` est plausible, puis stable.

Une porte qui échoue → stop, investigation, et au besoin repli
(l'instance legacy est intacte).

## 6. Basculer sur le profil réel

1. Éditer `etc/production.ini` : retirer/commenter le bloc de réveil —
   les réglages SMTP réels remplacent `pyramid_mailer.debug`, le
   service SMS réel remplace le puits.
2. Redémarrer ; contrôle de fumée d'un mail sortant sur un compte
   maîtrisé.
3. Basculer DNS/proxy vers la nouvelle instance.

## 7. Rollback

Tant que la bascule n'est pas validée : rebasculer DNS/proxy vers
l'instance legacy — elle n'a jamais été écrite. Conserver la
sauvegarde repozo et les copies extraites jusqu'à ce que la nouvelle
instance ait survécu à son premier vrai cycle de production.

## 8. Jalon de version (après coup)

Survivre au premier vrai cycle de production EST l'événement de
version. Ensuite :

1. Taguer les quatre dépôts aux shas déployés :

   ```bash
   for r in dace pontus daceui KuneAgi; do
     (cd $r && git tag -a v2.0.0 -m "First production cycle survived on the modern stack" && git push origin v2.0.0)
   done
   ```

2. Exécuter les merge-backs vers l'organisation `ecreall` : simples
   pushes fast-forward pour les trois bibliothèques, coutures
   d'adoption (`-s ours`, tip historique en parent) pour KuneAgi et
   nova-ideo — une seule annonce cohérente pour les deux foyers.
