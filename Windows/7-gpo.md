[Retour à la table des matières](../README.md)

# GPO et politiques de sécurité

Gestion centralisée des règles et configuration sur tout un domaine.

Forcer les GPO : gpupdate /force

Server Manager > Tools > Group policy management

## Ajouter une GPO

Ajouter une GPO dans le dossier Group Policy Objects

Une fois la GPO créée, il va falloir la lier à une OU (Unité organisationnelle)

![alt](images/gpo.png)

## Editer une GPO

Clic-droit éditer

> Attention, on ne mélange pas les User Configuration avec les Computer Configuration

## Stratégie Courantes

### Connecter un lecteur réseau

User Configuration > Preferences > Windows Settings > Drive Maps

### Exécuter un script

User Configuration > Preferences > Windows Settings > Scripts > Logon

> Les scripts sont lancés après 5 minutes (Pour changer il faut modifier une GPO Computers > Configure Logon Script  Delay)

### Permettre la connexion d’un utilisateurs sur le controleur de domaine

Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > User R > Allo logon on locally > Add User

### Empecher de voir qui est le dernier utilisateur de la machine

Computer Configuration > Policies > Windows Settings > Security Policies > Local Policies > Security Options > Interactive logon: Don’t display last signed-in

### Redirection de dossier

User Configuration > Policies > Windows Settings > Folder Redirection > Desktop >

![alt](images/gpo2.png)

### Redirection ordinateur obligatoire

Computer Configuration > Policies > Administrative Template > 

System > Group Policy > Configure folder redirection policy processing > enabled > process even if the group …

### Interdir le CMD

User Configuration > Policies > Administrative Template > System > Prevent access to the command prompt

## Limiter la portée d'une GPO

Pour modifier la portée à un certain groupe on peut modifier le sécurity filtering

> Attention il faut obligatoirement ajouter "Domain Computers" dans l'onglet Delegation

![alt](images/gpo3.png)

Ajouter une exception pour les ADMIN

Delegation > Advanced > Domain Admins > Apply group policy > Deny

![alt](images/gpo4.png)