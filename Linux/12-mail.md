[Retour à la table des matières](../README.md)

# Le service Mail

Envoi et échange de mails en utilisant le protocole SMTP (ports 25/465/587)

Réception des mails par les utilisateurs via POP3 (ports 110 ou 995 si TLS) ou IMAP (ports 143 ou 993 si TLS)

Par défaut, tous les utilisateurs créés (avec **useradd**) ont une boite mail personnelle.

> L'emplacement des fichiers mails des utilisateurs `/var/spool/mail/<login>`

Le fichier peut être créer mais il faut lui donner les permissions **-rw-rw----** avec le groupe mail

```
touch swila
chown swila.mail swila
chmod 0660 swila
```

## Configuration

Configuration principalement dans `/etc/postfix`

1. main.cf: configuration du service mail
2. virtual: Lien entre les adresses mails et les comptes utilisateurs

| Option | Explication |
| - | - |
| myhostname, mydomain | Spécifie le nom de l'hôte |
| inet_interfaces, inet_protocols | Mentionne les interfaces réseaux. Nous pouvons placer **all** à ces deux options |
| mydestination | Détermine quand un mail est arrivé à destination |
| mynetworks | Détermine qui peut accéder au serveur mail pour l'expédition. Il faut limiter l'accès aux machines du réseau (pas de open relay) ex: mynetworks = 172.18.1.0/24 |
| mail_spool_directory | Chemin vers les boites mails |

### Configuration des domaines virtuel

```
virtual_alias_domain = swi.la, swinnen.eu
virtual_alias_maps = hash:/etc/postfix/virtual
```

Il faut écrire dans le fichier `/etc/postfix/virtual` la liste des adresses:

```
postmaster@swi.la   swila
postmaster@swinnen.eu   swila
louis@swinnen.eu    lswinnen
mygod@swi.la    lswinnen, l.swinnen@helmo.be
```

Nous allons générer un fichier binaire grâce au fichier texte créer précédemment.

```
postmap /etc/postfix/virtual
```

Activer la configuration

```
systemctl restart postfix
```

### Exemple

```
myhostname = localhost.localdomain
mydomain = localdomain

inet_interfaces = all
inet_protocols = all

mynetworks = 172.18.1.0/24, 127.0.0.0/8

mail_spool_directory = /var/spool/mail

virtual_aliasçdomain = swi.la, swinnen.eu
virtual_alias_maps = hash:/etc/postfix/virtual
```

## Client Mail

Installer le client mail mailx

### Envoyer un mail

```
mail postmaster@swi.la
```

> Un mail finit par un point sur une autre ligne.

## Configuration Dovecot (Réception de mail)

La configuration de dovecot est localisée dans le fichier `/etc/dovecot/dovecot.conf` et dans le dossier `/etc/dovecot/conf.d`

Démarrer le service dovecot

```
systemctl start dovecot
```

dovecot.conf

```
protocols = imap pop3

listen = *, ::

login_greeting = Oui allo j'ecoute ?
```

```
cd /etc/dovecot/conf.d
```

10-auth.conf

```
disable_plaintext_auth = no
auth_username_format = %Lu
```

vim 10-mail.conf

```
mail_location = mbox:~/mail:INBOX=/var/spool/mail/%u
```

vim 10-ssl.conf

```
ssl = required, yes, no
```

Redémarrer dovecot

```
systemctl restart dovecot
```

## Lire un mail

```
telnet 172.18.1.2 110
```