#! /usr/bin/python3.9
import sys
import subprocess
import csv
import re

quotas = {"Compta": "130m", "Soins": "140m"}

with open("./liste-utilisateurs-password.csv", "r", encoding='utf-8') as input:
    csvreader = csv.reader(input, delimiter=";")
    for user in csvreader:

        name = user[0]
        firstName = user[1]
        departement = user[2]
        matricule = user[3]
        password = user[4]

        if departement in quotas:
            quota = quotas[departement]
        else:
            quota = "200m"

        result = subprocess.run(
            f"xfs_quota -x -c 'limit bhard={quota} {matricule}' /home", stdout=subprocess.PIPE, shell=True)
