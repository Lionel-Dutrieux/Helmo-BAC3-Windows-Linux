[Retour à la table des matières](../README.md)

# Introduction à Powershell

Il existe plusieurs façon d'écrire des scripts Powershell, la première consiste à utiliser Powershell ISE qui est déjà installé dans Windows Server, la seconde est Visual Studio Code avec l'extension Powershell.

## Sécurité

Les scripts Powershell pouvant être dangereux il n'est pas possible de base d'éxécuter des scripts provenant d'internet.

Pour permettre l'éxécution de script non sécurisé utilisez la commande:

```powershell
Set-ExecutionPolicy Unrestricted
```

## Variables

Les variables commencent par **$**

```powershell
[string] $name = "Lionel"
```

Powershell utilise un typage dynamique, il est possible de **forcer le type** de la donnée attendu.

| Type        | Description                                       |
|-------------|---------------------------------------------------|
| [string]    | Une chaîne de carractères                         |
| [char]      | Un caractère                                      |
| [byte]      | Un caractère codé sur 8 bits                      |
| [bool]      | Une valeur booléenne                              |
| [int]       | Un entier signé (32 bits)                         |
| [long]      | Un entier signé (64 bits)                         |
| [decimal]   | Un nombre décimal (128 bits)                      |
| [single]    | Une donnée en virgule flottante codée sur 32 bits |
| [DateTime]  | Une date et heure                                 |
| [array]     | Un tableau                                        |
| [hashtable] | Dictionnaire clé-valeur                           |

## Tableaux et tables hachées

Un tableau peut contenir des éléments de types différents

```powershell
$tab = @(1, "Test", $false, @{"cle1"="val1"; "cle2"="val2"})

Write-Output "Le second élément est $($tab[1])"
```

Utilisation d'une table hashée (dictionnaire)

```powershell
$dictionnaire = @{"cle"="valeur"; "cle2"="val2"}

$dictionnaire.Add("CLE3", "VAL3")
$dictionnaire["CLE3"] = "newVal"

$dictionnaire.Remove("CLE3")
$dictionnaire.ContainsKey("cle")
$dictionnaire.ContainsValue("val2")
```

## Opérateurs de comparaison

| Opérateur | C# | Description                                                         |
|-----------|----|---------------------------------------------------------------------|
| -eq       | == | Vérifie si 2 chaînes sont identiques                                |
| -ne       | != | Vérifie si 2 chaînes sont différentes                               |
| -ge       | >= | Vérifie si la première chaîne est plus grande ou égale à la seconde |
| -gt       | >  | Vérifie si la première chaîne est plus grande que la seconde        |
| -lt       | <  | Vérifie si la première chaîne est plus petite que la seconde        |
| -le       | <= | Vérifie si la première chaîne est plus petite ou égale à la seconde |
| -match    |    | Vérifie si la chaîne correspond à l'expression régulière renseignée |

## Méthodes

**Get-Random** tire un nombre entier positif de 32 bits compris entre 0 et 2147483647

```powershell
Get-Random -Minimum 4 -Maximum 20
```

**Read-Host** permet de lire une entrée au clavier

```powershell
[int] $monentier = Read-Host "Entrez un entier"
```

**Write-Output** affiche du texte à l'écran

```powershell
Write-Output "Hello World!"
```

**Get-Content** permet de lire un fichier texte

```powershell
$contenu = Get-Content "C:\TEMP\exemple.csv"
```

**Import-Csv** permet de lire directement un fichier au format CSV. Le résultat est un tableau donc chaque élément contient un dictionnaire

> La cmdlet suppose que le fichier CSV proposé contient une ligne de titre

```powershell
$contenu = Import-Csv -Path .\Processes.csv -Delimiter ;
```

**New-Item** permet de créer un dossier

```powershell
New-Item -ItemType "directory" -Path "C:\MonDossier"
```

**Set-Location** se placer dans un dossier

```powershell
Set-Location "C:\Temp"
```

Exécution directe et récupération du résultat dans une variable

```powershell
$resultat = &"tasklist.exe"
```

## Gestion des erreurs

Powershell autorise des blocs try/catch

Pour obliger le passage dans le bloc **catch** pour toutes les erreurs il faut ajouter le paramètre -ErrorAction Stop à la cmdlet Get-Content

```powershell
try {
    $contenu = Get-Content "C:\TEMP\exemple.csv"
    Write-Output "OK!"
} catch {
    Write-Output "Fichier non trouvé"
}
```

## Exemples

Parcourir un fichier texte (.csv) avec une expression régulière

```powershell
$contenu = Get-Content "C:\TEMP\exemple.csv"

foreach ($ligne in $contenu) {
    if ($ligne -match '^([^;]+);([^;]+);([^;]+)$') {
        ...
    }
}
```

Générer un mot de passe aléatoire ([generatePassword.ps1](scripts/generatePassword.ps1))

```powershell
$pass = &"./generatePassword.ps1" -length 8 -maxNumber 2 -maxUpper 2
```