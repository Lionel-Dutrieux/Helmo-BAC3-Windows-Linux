#! /usr/bin/python3.9
import sys
import subprocess
import csv
import re

reg = r"(0*)(\d+)"

existingGroup = []

uniqueId = 20000


def getId():
    global uniqueId
    uniqueId = uniqueId + 1
    return uniqueId


with open("./liste-utilisateurs-password.csv", "r", encoding='utf-8') as input:
    csvreader = csv.reader(input, delimiter=";")
    for user in csvreader:

        name = user[0]
        firstName = user[1]
        departement = user[2]
        matricule = user[3]
        password = user[4]

        num = re.findall(reg, matricule)
        num = int(num[0][1])

        if num % 2 == 0:
            subprocess.call(
                f"./mkglobal-user.py \"{name}\" \"{firstName}\" \"{getId()}\" \"{matricule}\" \"{password}\"", shell=True)
            result = subprocess.run(
                f"mkdir /home/{matricule}", stdout=subprocess.PIPE, shell=True)
            result = subprocess.run(
                f"chmod 700 /home/{matricule}", stdout=subprocess.PIPE, shell=True)
            result = subprocess.run(
                f"chown {matricule}:users /home/{matricule}", stdout=subprocess.PIPE, shell=True)
        else:
            result = subprocess.run(
                f"useradd -g users \"{matricule}\"", stdout=subprocess.PIPE, shell=True)
            result = subprocess.run(
                f"echo -e \"{password}\n{password}\" | passwd {matricule}", stdout=subprocess.PIPE, shell=True)

        if departement not in existingGroup:
            result = subprocess.run(
                f"groupadd {departement.lower()}", stdout=subprocess.PIPE, shell=True)
            existingGroup.append(matricule)

        result = subprocess.run(
            f"usermod -G \"{departement.lower()}\" \"{matricule}\"", stdout=subprocess.PIPE, shell=True)
