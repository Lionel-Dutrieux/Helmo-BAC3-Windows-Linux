[Retour à la table des matières](../README.md)

# Sauvegarde, planification et installation

## Sauvegarder des fichiers

### ZIP

```
zip -r /tmp/save-etc.zip /etc/*
unzip monfichier.zip
unzip -l monfichier.zip (Lister les fichiers)
```

### TAR.GZ

#### Création d'une archive

```
tar cvzf /tmp/save-etc.tar.gz /etc (gzip)
tar cvjf /tmp/save-etc.tar.gz /etc (bzip2)
tar cvJf /tmp/save-etc.tar.gz /etc (xz)
```

#### Extraction d'une archive

```
tar xvzf /tmp/save-etc.tar.gz /etc (gzip)
tar xvjf /tmp/save-etc.tar.gz /etc (bzip2)
tar xvJf /tmp/save-etc.tar.gz /etc (xz)
```

#### Lister les fichiers contenus dans une archive

```
tar tvzf /tmp/save-etc.tar.gz /etc (gzip)
tar tvjf /tmp/save-etc.tar.gz /etc (bzip2)
tar tvJf /tmp/save-etc.tar.gz /etc (xz)
```

## Sauvegarde de fichiers

`scp` permet de copier un ou plusieurs fichiers vers une machine distante.

`rsync` permet de synchroniser un dossier avec une machine distante

`lftp` permet de copier, par ftp, des fichiers ou dossiers

### Sauvegarde par SCP

```
scp monfichier.tar.gz e190061@dartagnan.cg.helmo.be:/tmp
```

### Sauvegarde par RSYNC

```
rsync -avz /home e190061@dartagnan.cg.helmo.be:~/backup -e ssh
```

## Planification des tâches

### Tâches ponctuelles

```
at 15:20
/usr/sbin/reboot

CTRL + D
```

Planification possibles

- at 15:3007192021
- at 15:30 jul 19 2021
- at now + 5 hours
- at now + 1 day
- at 11:20 next month
- at 22:00 tomorrow


### Tâches répétitives (CRON)

```
crontab -e
```

> M H j m J commande

Avec:

- M représentant la minute
- H représentant l’heure
- j représentant le jour
- m représentant le mois
- J représentant le jour de la semaine.
- commande représentant la commande à exécuter

## Installation d'application

```
dnf upgrade
dnf install xterm
dnf search php
dnf install ./monfichier.rpm
```

Applications fournies sous la forme de fichiers source

1. Télécharger l'application depuis internet (souvent archive .tar.gz) Il faut décompresser l'archive
2. Compilation de l'application
3. Installation de l'application (en root)

Compilation:

```
cd dossier_application
./configure
make
```

Installation:

```
make install
```
