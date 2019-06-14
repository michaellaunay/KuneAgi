Pour consulter les logs :

    tail -f /home/docker/volumes/postfix/log/mail.log


Pour consulter les logs d'erreur :

    tail -f /home/docker/volumes/postfix/log/mail.err


Les permissions des clés doivent appartenir à l'uid 105 :

    user@server:~/dockerfiles/postfix$ ls -lR assets/
    assets/:
    total 16
    drwxr-xr-x 2 root root 4096 sept. 23  2016 certs
    drwxr-xr-x 2 root root 4096 sept. 23  2016 domainkeys
    -rwxr-xr-x 1 root root 4474 juin  13  2017 install.sh

    assets/certs:
    total 4
    -rw-r--r-- 1 root root 55 sept. 23  2016 readme

    assets/domainkeys:
    total 20
    -r-------- 1 messagebus mlocate 1675 sept. 23  2016 nova-ideo.private
    -rw-r--r-- 1 root       root     504 sept. 23  2016 nova-ideo.txt
    -rw-r--r-- 1 root       root      40 sept. 23  2016 readme
