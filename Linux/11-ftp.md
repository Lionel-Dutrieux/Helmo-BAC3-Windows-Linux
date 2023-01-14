[Retour à la table des matières](../README.md)

# Le service FTP

Le service FTP n'est pas sécurisé par défaut.

Il y a 2 modes de fonctionnement

- FTP actif
- FTP passif # Préféré

## Configuration

```
vim /etc/vsftpd
```

| Option | Excplication |
| - | - |
| anonymous_enable | Autorise la connexion en anonyme |
| local_enable | Les utilisateurs locaux peuvent se connecter |
| write_enable | Permet l'écriture, il faut avoir les bon ACL |
| local_umask | Permission à la creation du fichier |
| dirmessage_enable | Affiche une message lors de la connexion |
| ftpd_banner | Login message |
| chroot_local_user | Permet aux utilisateurs d'écrire |
| listen=YES | Ecoute en IPV4 |
| listen_ipv6=NO | Ecoute en IPV6 |
| userlist_enable=YES | |
| userlist_deny=YES |  |
| userlist_file |  |
| pasv_min_port=10000 | Port minimal pour le NAT |
| pasv_max_port=15000 | Port maximal pour le NAT |
| pasv_address=1.2.3.4 | Adresse IP WAN |
| ssl_enable=YES | Active SSL |
| rsa_cert_file | Chemin du certificat eu format .pem |
| rsa_private_key_file | Chemin  de la clef privé .pem |

> Attention problème avec le NAT et l'IPV6

Si chroot_local_user=YES et que chroot_list_enable=NO == TOUT les utilisateurs sont emprisonné dans leurs dossier personnel.

Si chroot_local_user=YES et que chroot_list_enable=YES == TOUT les utilisateurs sont emprisonné dans leurs dossier personnel sauf ceux qui sont mentionné dans le chroot_list_file.

Si chroot_local_user=NO et chroot_list_enable=YES == Seul les utilisateurs mentionné dans le fichier chroot_list_file seront emprisonné dans leurs dossier personnel.

Si userlist_enable=YES et userlist_deny=YES == Tous les utilisateurs connus sont autorisé a se connecter sur le serveur excepté ceux mentionné dans le userlist_file.

Si userlist_enable=YES et userlist_deny=NO == Seul les utilisateurs connu et listé dans le userlist_file peuvent se connecter au serveur.

Si userlist_enable=NO == Tous les utilisateurs connu du système peuvent se connecter au serveur.

### Appliquer la configuration

```
systemctl restart vsftpd
```

### Debug un fichier vsftpd

```
vsftpd /etc/vsftpd/vsftpd.conf
```

## Client FTP

### Installation

```
dnf install ftp lftp
```

### Utilisation

```
ftp

open 192.168.1.200

ls

cd

get videolan

put send file

lcd /tmp # Local cd

prompt # Active ou désactive l'interraction entre fichiers

exit
```

## Le service lftp

Permet le scripting FTP

```
lftp login:pass@192.168.1.200 -e "cd dossier; put fichier; exit;"
```