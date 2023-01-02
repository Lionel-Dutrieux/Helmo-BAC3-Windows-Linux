[Retour à la table des matières](../README.md)

# Introduction à Python

Par défaut les scripts python ne sont pas exécutable, pour les rendre exécutables il faut modifier les droits d'exécution

```
chmod +x script.py
```

Dans chaque script il faut indiquer où se trouve l'emplacement de python

```
#! /usr/bin/python3.9
# Commentaire: Hello World !
```

## Les variables

```python
i=2
f=10.5
chaine="ma chaine"
val=False
jours = ["lundi", "mardi", False]
jours[2] = "mercredi"
semaine = { "travail": ["lundi", "mardi"], "weekend": "dimanche" }
```

## Récupérer les arguments

`sys.argv` est une liste contenant tous les paramètres du script Python

## Modules

| Module | Explication |
| --- | --- |
| os | permet la manipulation de fichiers et dossiers, changement de répertoires, modification permissions, création de processus |
| sys | Accès aux paramètres de la ligne de commandes, identification et information du SE |
| subprocess | permet l’exécution de programme externe en récupérant le résultat dans le script Python |
| re | permet l’utilisation d’expression régulière dans le script Python |

```python
import module1

module1.function1()
```

## Les opérations

L’opération n++ ou n— n’existe pas en python

## Les chaines de caractères

```python
f"{c1} {c2}"

c1.split(sep) # Retourne une liste en fonction du separateur
"sep".join(lst) # Rassemble une chaîne
```

## Les entrées et sorties

```python
prenom = input("Entrez votre prenom:")
age = int(input("Entrez votre age:"))

print(f"Bonjour {prenom}, vous avez {age} ans !")

with open('monfichier.txt', "r") as fichier:
 for ligne in fichier:
	 print(f"Ligne lue > {ligne.rstrip()}")

with open("./copie.txt", "w") as sortie, open("./original.txt", "r") as entree:
    for ligne in entree:
        sortie.write(ligne)
```

Méthode d'accès pour accéder à un fichier

| Droit | Explication |
| --- | --- |
| r | readonly |
| r+ | readonly and write |
| w | write only |
| w+ | write and read |
| a | append only |
| a+ | append and read |

## Les expressions régulières

| Symbole | Explication | Symbole | Explication |
| --- | --- | --- | --- |
| \s | Espace ou tabulation | \w | Alphanumérique ou _ |
| \S | Ni espace, ni tabulation | \W | Ni alphanumérique, ni _ |
| \d | Un chiffre | ^ | 1er élément de la ligne |
| \D | Tout sauf un chiffre | $ | Doit terminer la ligne |
| (a \| b) | Caractère a ou b | a | Le caractère a |
| a+ | Répétition 1-N de a | (ab)+ | Répétition 1-N de ab |
| a* | Répition 0-N de a | [^abc] | Ni a, ni b, ni c |
| [a-z] | Une lettre minuscule | . | Un caractère quelconque |
| () | Grouper / cibler une valeur |  |  |

```python
import re
data = "Louis;SWINNEN;Campus Guillemins;Rue de Harlez;35;400;Liege;"

reg = r"^\s*(.*);([^;]+);((\w|\s)*);(\D*);(\d*);(\d*);([A-Z]*);$"

pattern = re.compile(reg)
match = pattern.match(data)
if match:
    for i in range(len(match.groups()) + 1):
        print(f"[{index}] = {match.group(index)}")
```

## Exécution d'une commande

```python
import subprocess
cmd = "ps -ef | wc -l" # On Compte le nbre de processus
result = subprocess.run(cmd, stdout=subprocess.PIPE, shell = True)

print(f"Nombre de processus = {result.stdout.decode().rstrip()}")
```

## Exemples

### Lire & Ecrire un fichier CSV

```python
import csv

with open("./liste-utilisateurs.csv", "r", encoding='utf-8') as csvfile, open("./liste-utilisateurs-2.csv", "w", encoding='utf-8', newline='') as output:
    csvreader = csv.reader(csvfile, delimiter=";")
    csvwriter = csv.writer(output, delimiter=";")
    for row in csvreader:
        print(row)
        row.append("matricule")
        row.append("password")
        csvwriter.writerow(row)
```