#! /usr/bin/python3.9
# mkglobal-user.py "DUTRIEUX" "Lionel" 20500 "e190061" "rootroot"
import sys
import subprocess

filePath = "/tmp/tempUser.ldif"


def hashPassword(passwd):
    slappasswdCommand = f"slappasswd -s {passwd}"
    result = subprocess.run(
        slappasswdCommand, stdout=subprocess.PIPE, shell=True)
    hashPassword = result.stdout.decode().rstrip()
    return hashPassword


def addUserLDAP(filePath):
    ldapaddCommand = f"ldapadd -D 'cn=Directory Manager,dc=localdomain' -f '{filePath}' -x -w rootroot "
    result = subprocess.run(ldapaddCommand, stdout=subprocess.PIPE, shell=True)
    print(result.stdout.decode().rstrip())


def createLdifFile(filePath):
    name = sys.argv[1]
    surname = sys.argv[2]
    uid = sys.argv[3]
    login = sys.argv[4]
    passwd = hashPassword(sys.argv[5])

    file = f"""dn: uid={login}, ou=People,dc=localdomain
objectClass: top
objectClass: inetorgperson
objectClass: posixAccount
cn: {surname} {name}
sn: {name}
givenname: {surname}
userPassword: {passwd}
gidNumber: 100
uidNumber: {uid}
homeDirectory: /home/{login}
loginShell: /bin/bash"""

    with open(filePath, "w") as fichier:
        fichier.write(file)
        fichier.close()


def checkArgs():
    nbArgs = len(sys.argv)
    return nbArgs == 6


if checkArgs():
    createLdifFile(filePath)
    addUserLDAP(filePath)
else:
    print("Missing arguments")
