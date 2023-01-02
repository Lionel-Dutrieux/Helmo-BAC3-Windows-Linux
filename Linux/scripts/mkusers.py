#! /usr/bin/python3.9
import sys
import subprocess
import csv
import re

reg = r"(0*)(\d+)"

existingGroup = []

with open("./liste-utilisateurs-password.csv", "r", encoding='utf-8') as input:
    csvreader = csv.reader(input, delimiter=";")
    for user in csvreader:

        num = re.findall(reg, user[3])

        if int(num[0][1]) % 2 == 0:
            subprocess.call(
                f"mkglobal-user.py {user[0]} {user[1]} {20000 + num[0][1]} {user[3]} {user[4]}", shell=True)
        else:
            result = subprocess.run(
                f"useradd -g users {user[3]}", stdout=subprocess.PIPE, shell=True)

            result = subprocess.run(
                f"echo {user[4]} | passwd {user[3]}", stdout=subprocess.PIPE, shell=True)

        if user[2] not in existingGroup:
            result = subprocess.run(
                f"groupadd {user[2].lower()}", stdout=subprocess.PIPE, shell=True)
            existingGroup.append(user[2])

        # Ajoute l'utilisateur au groupe
        result = subprocess.run(
            f"usermod -G {user[2].lower()} {user[3]}", stdout=subprocess.PIPE, shell=True)
