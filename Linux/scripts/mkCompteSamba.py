#! /usr/bin/python3.9
import subprocess
import sys
import csv


def add_samba_user(username, password):
    subprocess.run(
        f"echo -e \"{password}\n{password}\" | smbpasswd -a {username}", stdout=subprocess.PIPE, shell=True)


with open("./liste-utilisateurs-password.csv", "r", encoding='utf-8') as input:
    csvreader = csv.reader(input, delimiter=";")
    for row in csvreader:
        add_samba_user(row[3], row[4])
