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
| chroot_local_user | Permet d |
| chroot_list_file |  |

20:08