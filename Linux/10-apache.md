[Retour à la table des matières](../README.md)

# Le serveur web Apache

## Les fichiers de configuration

Configuration globale d’Apache

```
vim /etc/httpd/conf/httpd.conf
```

Configuration par site

```
vim /etc/httpd/conf.d
```

Le fichier `ssl.conf` propose la configuration par défaut pour le support TLS

## Fichier `httpd.conf`

| Option | Explication |
| - | - |
| ServerRoot | Mentionne le chemin vers la configuration du serveur |
| Listen | Mentionne les ports d'écoute |
| Include conf.modules.d/*.conf | Inclut tous les fichiers .conf se trouvant dans le dossier conf.modules.d |
| User apache Group apache | Indique le nom d'utilisateur et le groupe sous lequel le processus Apache est démarré. Il ne faut JAMAIS indiquer root, il faut préciser un utilisateur avec les bon ACL |
| ServerAdmin | Mentionne l'addresse mail de l'administrateur. Peut être inclus sur les pages d'erreur générées par le serveur |
| ServerName | Mentionne le nom DNS du serveur Apache. On peut remplacer celui-ci par son adresse IP si aucun nom DNS n'est associé |
| DocumentRoot | Indique l'emplacement du site web par défaut `/var/www/html` |
| Directory | Précise des options, des autorisations ou restrictions au dossier, la directive `Options` avec les paramètres `Indexes` qui affiche les fichier en l'absence d'une page d'index ou `FollowSymLinks` qui permet de suivre des liens, la directive `AllowOverride` permet de supporter les fichier .htaccess qui modifie localement la configuration du serveur, l'option `Require` qui mentionne qui peut accéder au dossier |
| AddDefaultCharset | Indique le codage de caractères par défaut utilisé. `AddDefaultCharset UTF-8` |

## Dossier `conf.d`

Tous les fichiers `.conf` sont pris en compte. Peut contenir des fichiers différents par site.

Le nom du fichier importe peu tant que l'extension est .conf

> /!\ Le DNS doit être configuré pour que le nom mentionné pointe vers l'IP du serveur.

### Exemple

```xml
<VirtualHost 192.168.3.206:80 [2001:6a8:2cc0:8000::206]:80>
    ServerName project.helmo.be
    ServerAlias webmail.helmo.be
    DocumentRoot /var/www/html/default
    <Directory "/var/www/html/default" >
        AllowOverride All
        Options FollowSymLinks
        Require all granted
    </Directory>
    ErrorLog logs/error_log
    CustomLog logs/access_log combined
</VirtualHost>
```

## Activer TLS

Pour activer TLS, il faut disposer:

- D'un certificat associé au nom DNS à sécuriser. Le certificat doit être déposé dans le dossier `/etc/pki/tls/certs`
- Des certificats intermédiaires permettant de créer un chemin de confiance vers l'autorité racine. Il convient de placer ces certificats dans le dossier `/etc/pki/tls/certs`
- La clé privée associé au certificat, elle doit être déposée dans le dossier `/etc/pki/tls/private`. Protéger celle-ci avec les permissions restrictives: droits `0600` et propriétaire `root:root:`

Fichier à modifier `/etc/httpd/conf.d/ssl.conf`

- Modifier le site par défaut VirtualHost _default_:443
- Les options vues précédemment s'appliquent également ici

Voici les options recommandé par [Mozilla.org](https://ssl-config.mozilla.org)

- SSLEngine: Active ou non le support TLS `SSLEngine on`
- SSLProtocol: restreins le support TLS à certaines versions `SSLProtocol all -SSLv2 -SSLv3 -TLSv1 -TLSv1.1 TLSv1.2`
- SSLCipherSuite: Liste les algorithmes acceptés lors du TLS Handshake
  
Ajouter l'option `SSLCertificateFile` chemin vers le certificat du site ainsi que `SSLCertificateKeyFile` avec la clé privé du certificat, `SSLCertificateChainFile` chemin vers les certificats intermédiaires

### Exemple

```xml
<VirtualHost *:443>
	ServerName example.com
	ServerAlias www.example.com
	ServerAdmin admin@example.com

	DocumentRoot /var/www/example.com/html
	<Directory /var/www/example.com/html>
		Options -Indexes +FollowSymLinks
		DirectoryIndex index.php
		AllowOverride All
		Require all granted
	</Directory>

	SSLEngine on
	SSLProtocol -all +TLSv1.2
	SSLCertificateFile /etc/letsencrypt/live/example.com/fullchain.pem
	SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem
	Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>
```

## Authentification simple

Il faut activer la prise en charge des fichiers .htaccess (Voir `AllowOverride`)

Créer un fichier `.htaccess` à la racine du site à protéger

Créer les utilisateurs autorisés à se connecter

> /!\ Attention TLS doit être activé pour éviter d'envoyer les mots de passe en clair.

### Exemple `.htaccess`

```
AuthType Basic
AuthName "Message affiché"
AuthBasicProvider file
AuthUserFile "/var/www/admin.pass"
Require valid-user
```

Création des utilisateurs:

```
htpasswd -B -c /var/www/admin.pass admin
htpasswd -B -c /var/www/admin.pass e190061
```

## Sites web personnels

Permets à des utilisateurs de déposer un site web `http://ip/~loginUser`

Fichier `/etc/httpd/conf.d/userdir.conf`

Il faut enlever le commentaire #UserDir public_html

> Vérifier les ACL pour que le groupe Apache puisse acceder /home/login/public_html

## Service

```
systemctl restart httpd
```