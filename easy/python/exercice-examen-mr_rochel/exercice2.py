#! /usr/bin/env python
""" 
Ecrire un programme en python qui effectue les operations suivantes:

a- Invitez l'utilisateur à entrer le nom, l'age et sexe de n etudiants via le console du System
b- Enregistrez les informations de ses etudiants dans un fichier nommée etudiant.txt
c- filtrer les informations des etudiants de type feminin dans le fichier etudiant.txt et les transettre dans etudiants.feminin.txt
d- filtrer les informations des etudiants de type masculin dans le fichier etudiant.txt et les transmettre dans etudiant.masculin.txt
"""

# START : 08"05

#! a- Invitez l'utilisateur à entrer le nom, l'age et sexe de n etudiants via le console du System

numberEtudiant = int(input("Entrer le nombre étudiant : "))
etudiantList = []
for i in range(numberEtudiant):

    nom = str(input(f"Entrez le nom de l'élève numéro {i} : "))
    age = int(input(f"Entrez son age : "))
    sexe = str(input("Entrez son sexe (f/m) : "))

    etudiantList.append( {
        'nom':nom,
        'age':age,
        'sexe':sexe
    } )

#! b- Enregistrez les informations de ses etudiants dans un fichier nommée etudiant.txt
myEtudiantFile = open("Etudiant.txt", "w")
myEtudiantFile.write("nom/age/sexe/\n")
for i in range(len(etudiantList)):
    formatedData = f"{etudiantList[i]['nom']}/{etudiantList[i]['age']}/{etudiantList[i]['sexe']}/\n"
    myEtudiantFile.write(formatedData)

myEtudiantFile.close

#! c- filtrer les informations des etudiants de type feminin dans le fichier etudiant.txt et les transettre dans etudiants.feminin.txt
#! d- filtrer les informations des etudiants de type masculin dans le fichier etudiant.txt et les transmettre dans etudiant.masculin.txt

myEtudiantFile = open("Etudiant.txt","r")
myEtudiantDatas = myEtudiantFile.readlines()

feminFile = open("Etudiant.fem.txt", "a")
mascFile = open("Etudiant.masc.txt", "a")

for i in range(1,len(myEtudiantDatas)):
    etudiantData = myEtudiantDatas[i].split("/")
    if etudiantData[2] == "f":
        feminFile.write(myEtudiantDatas[i])
    elif etudiantData[2] == "m":
        mascFile.write(myEtudiantDatas[i])

feminFile.close()
mascFile.close()
myEtudiantFile.close()

# FINISH : 08"55