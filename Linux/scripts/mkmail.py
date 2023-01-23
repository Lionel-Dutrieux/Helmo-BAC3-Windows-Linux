#! /usr/bin/python3.9
import sys
import subprocess
import os
import csv

email_list = []

DOMAIN = "dutrieux.swilabus.com"


def make_email(first_name, last_name, domain):

    # Removing spaces and dashes, and converting to lowercase
    first_name = first_name.replace(" ", "").replace("-", "").lower()
    last_name = last_name.replace(" ", "").replace("-", "").lower()

    # Removing accent
    first_name = first_name.encode('ascii', 'ignore').decode()
    last_name = last_name.encode('ascii', 'ignore').decode()

    # Taking the first letter of the first name
    email_username = first_name[0]
    email_username += "." + last_name

    email_address = email_username + "@" + domain

    count = 2

    while email_address in email_list:
        email_username = first_name[:count] + "." + last_name
        email_address = email_username + "@" + domain
        count = count + 1

    email_list.append(email_address)
    return email_address


def createMail(login):
    mail_file = f"/var/spool/mail/{login}"
    if not os.path.exists(mail_file):
        subprocess.run(f"touch {mail_file}",
                       stdout=subprocess.PIPE, shell=True)
        subprocess.run(f"chown {login}:mail {mail_file}",
                       stdout=subprocess.PIPE, shell=True)
        subprocess.run(f"chmod 0660 {mail_file}",
                       stdout=subprocess.PIPE, shell=True)


with open("./liste-utilisateurs-password.csv", "r", encoding='utf-8') as input:
    csvreader = csv.reader(input, delimiter=";")
    for user in csvreader:
        first_name = user[0]
        last_name = user[1]
        login = user[3]
        email = make_email(first_name, last_name, DOMAIN)
        createMail(login)
        print(email)
