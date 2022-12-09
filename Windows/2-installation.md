[Retour à la table des matières](../README.md)

# Installation de Windows Server 2022

Sélectionnez **Windows Server 2022 Standard Evaluation (Desktop Experience)**

Wich type of installation do you want ? (**Custom**)

Entrez un mot de passe : P@ssword

## Configuration de Windows Server

- Changer le thème
- Désactiver le pare-feu
- Désactiver Windows Defender
- Installation des outils
- Configuration réseau
- Rôle et fonctionnalités

### Changer le thème

Settings > Theme > Desktop Icon Settings > ALL

### Désactiver le pare-feu

Windows Server Manager

Tools > Windows Defender Firewall with Advanced Security > Windows Defender Firewall Properties

Domain Profile: Firewall state **OFF**

Private Profile: Firewall state **OFF**

Public Profile: Firewall state **OFF**

### Désactiver Windows Defender

Server Manager

Local Server > 

Microsoft Defender Antivirus > Real-time protection > ALL **OFF**

IE Enhanced Security Configuration > **OFF**

### Installation des outils

VMWare > Install VMware Tools

### Configuration réseau

Server Manager

Local Server > IPV4 & IPV6 > Properties > Use the following IP address

> Ip address: 192.168.190.5
>
> Subnet mask: 255.255.255.0
> 
> Default gateway: 192.168.190.2 (Pfsense)

Changez les préférences DNS

> Preferred DNS server: 192.168.190.2 (Pfsense)

### Rôle et fonctionnalités

Server Manager

Manage > Add Roles and Features

> Attention les rôles et les features dépendent des exercices

- Windows Active Directory Domain Service
- DNS Server
- DHCP Server
- File Server Ressource Manager
- Windows Server Backup
