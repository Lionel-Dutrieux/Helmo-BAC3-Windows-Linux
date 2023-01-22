#! /usr/bin/python3.9
import subprocess
import sys
import csv


def add_samba_user(username, password):
    subprocess.run(["smbpasswd", "-a", username],
                   input=password, encoding='ascii')


with open("./liste-utilisateurs.csv", "r", encoding='utf-8') as input:
    csvreader = csv.reader(input, delimiter=";")
    for row in csvreader:
        add_samba_user(row[3], row[4])
