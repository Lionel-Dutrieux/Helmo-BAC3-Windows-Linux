#! /usr/bin/python3.9
import subprocess
import sys
import csv

mkpasswdCommand = "mkpasswd -l 15 -d 3 -c 3 -C 3 -s 0"

prefixCount = {}


def getPrefix(user):
    departement = user[2].lower()
    return f"{departement[0]}{departement[-1]}"


def addPrefix(prefix):
    if prefix in prefixCount:
        prefixCount[prefix] = prefixCount[prefix] + 1
    else:
        prefixCount[prefix] = 1


def getPassword(prefix):
    if prefixCount[prefix] == 1:
        return "Passw0rd"
    result = subprocess.run(
        mkpasswdCommand, stdout=subprocess.PIPE, shell=True)
    return result.stdout.decode().rstrip()


with open("./liste-utilisateurs.csv", "r", encoding='utf-8') as input, open("./liste-utilisateurs-password.csv", "w", encoding='utf-8', newline='') as output:
    csvreader = csv.reader(input, delimiter=";")
    csvwriter = csv.writer(output, delimiter=";")
    for user in csvreader:

        prefix = getPrefix(user)
        addPrefix(prefix)
        matricule = f"{prefix}{'%04d' % prefixCount[prefix]}"
        password = getPassword(prefix)
        user.append(matricule)
        user.append(password)

        csvwriter.writerow(user)
