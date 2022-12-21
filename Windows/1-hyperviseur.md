[Retour à la table des matières](../README.md)

# Démarrage de l'hyperviseur

> Attention, si vous travaillez sur une machine de l'école, utilisez bien le dossier c:\admsys pour enregistrer vos machines virtuelles

## Configurer le Virtual Network (VmWare)

Edit > Virtual Network Editor

> Info : VMnet0 en bridge mode connecte directement la machine virtuelle à une carte réseau

![VMnet1](images/vmware1.png)

> Info : VMnet1 en host-only permet de configurer un sous réseau appart du réseau physique (private network)

![VMnet8](images/vmware2.png)

> Info : VMnet8 en NAT permet de passer le trafic des machines virtuelles par l'adresse IP de l'hôte

## Ouvrir une machine virtuelle

Open a Virtual Machine

Storage path: c:\admsys\matricule\machine-name

## Configurer les machines virtuelles

### Pfsense

Changer le network adapter de brideged en **NAT**

### Windows Server

Installation avec un fichier iso

1. Create a Virtual Machine
2. Custom (advanced)
3. I will install the file operating system later
4. Select operating system > Microsoft Windows
5. Select version > Windows Server 2019
6. Virtual machine name > Win22SRV-1
7. Storage path > c:\admsys\matricule\machine-name
8. Network type > Use host-only networking
9. Maximum disk size > 30Gb
10. Store virtual disk as single file
11. Customize hardware >
    1.  Use ISO image
    2.  Remove sound card
    3.  Remove printer
