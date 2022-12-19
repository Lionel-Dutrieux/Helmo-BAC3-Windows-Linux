[Retour à la table des matières](../README.md)

# Espace disque, partage et droits

> Afficher les dossiers et fichiers cachés: View > Options > View (Hide empty drives & Hide extensions for known file types)

## Les volumes

Windows Server Manager

Tools > Computer Management > Disk Management

## Les droits ACL

![alt](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d2b4bd53-c2ff-4e44-8657-307969e0ae11/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221219T155111Z&X-Amz-Expires=86400&X-Amz-Signature=f9f89bc4c69acb7b8d37dcb312518140b974a7ad185b3525ad0c82b54f21abfe&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

![alt](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/436e1215-1df7-42d0-8e6b-211d06802a59/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221219T155154Z&X-Amz-Expires=86400&X-Amz-Signature=3eff1ebde535ad36d88607bb3363f31f39b08917c3fc1b44f3cb598bb1242ffa&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

![alt](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0a0e6a3b-fbd9-46e0-8bf6-ba46b7edbd6e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221219T155238Z&X-Amz-Expires=86400&X-Amz-Signature=fdd03e757336104570e6cf8f7732f7994b0b53848cfb7679ad70dcb98116069d&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

## Modification des permissions

Properties > Security > Edit

> Attention pour supprimer les permissions d'un dossier, il faut s'assurer de supprimer l'héritage (Disable inheritance => Convert)

```powershell
$acl = Get-ACL -Path "C:\TestACL" # Récupère les infos des ACL
$acl | select-Object * # Voir les infos

#Enlever l'héritage
$acl.SetAccessRuleProtection($true, $true) #Param 1 = Activer ou désactover l'hérotage (true = desac), Param 2 = conserver les permissions (true)
Set-Acl -Path "C:\TestAcl" $acl

# Ajouter des droits à un utilisateur
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("GODSWILA\Powerswila", "Modify", "Allow")
$acl.SetAccessRule($rule)
Set-Acl -Path "c:\TestAcl" $acl

$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("GODSWILA\Powerswila", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow")
```

![alt](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9af86443-4437-4e9c-9033-7794749dedc7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221219T161030Z&X-Amz-Expires=86400&X-Amz-Signature=58a823ddb6f94e776ddbd7ae11eba141ed9323eec163332d674eb6e00dd0715b&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

## Les quotas

> Attention ne pas utiliser les quotas avec les quotas sur un chemin en même temps.

This PC > Disk > Properties > Quota

- Enable quota management
- Deny disk space to users exceeding quota limit

Modifier les quotas pour certains utilisateurs

Quota Entries

```powershell
&"fsutil" "quota" "modify" "C:" "900 000000" "1000 000000" "powerswila"
```

## Quotas sur un chemin

Tools > File Server Resource Manager

Création de template de quota

Quota Template > Create Quota Template

Copy from existing template

Appliquer la template:

Quotas > Create Quota

Indiquer le path du dossier et selectionner une template

```powershell
New-FSRMQuota -Path "C:\testQuota" -Template "Limit150Mo"
New-FSRMAutoQuota -Path "C:\testQuota" -Template "Limit150Mo"
```

> Le quota automatique permet d'hériter le quota aux sous dossier.

## Les partages

Properties > Sharing > Advanced Sharing

Share this folder

Permissions > Remove Everyone

Add Authenticated Users (Cocher change)

> Ne pas oublier de modifier les ACLs

Acceder aux partages depuis une autre machine

Mapper une lettre au lecteur

```powershell
Cmd
net view \\MASTER # Affiche les partages
net use M: \\MASTER\TestPartage # Connect
```

## Les profils utilisateurs

Swilabus Réapropriation: 1:35:57

File Server Manager > Active Directory Users and Computers > User > Profile

- Profile path
- Home folder

![alt](images/profilepath.png)

> Il est impossible pour l’admin de rentrer dans le dossier monprof.V6 (Pour regler le probleme il faut créer le dossier à l’avance ou remplacer le owner par Administrator et replace all child object permission entries)

```powershell
# Parametre en plus de la commannde New-AdUser
-ProfilePath "\\MASTER\Sujets\jedi\monprof" -HomeDirectory "\\MASTER\Sujets\jedi\" -HomeDrive "K:"

Ou Set-AdUser
```