#! /usr/bin/env python
""" 
Ecrire un programme en python qui effectue les operations suivantes:

a- Invitez l'utilisateur à entrer le nom, l'age et sexe de n etudiants via le console du System
b- Enregistrez les informations de ses etudiants dans un fichier nommée etudiant.txt
c- filtrer les informations des etudiants de type feminin dans le fichier etudiant.txt et les transettre dans etudiants.feminin.txt
d- filtrer les informations des etudiants de type masculin dans le fichier etudiant.txt et les transmettre dans etudiant.masculin.txt
"""

# START : 08"05

class Exercice2:

    fileHeader = "NOM\t\t\t|\tAGE\t|\tSEXE\n"
    class Etudiant:

        def __init__(self,nom,age,sexe):
            self.nom = nom
            self.age = age 
            self.sexe = sexe

        def toString(self)->str:
            return f"{self.nom}\t\t|\t{self.age}\t|\t{self.sexe}\n"

        def getAllEtudiants()->list:
            myEtudiantFile = open("Etudiant.txt","r")
            myEtudiantDatas = myEtudiantFile.readlines()

            etudiantList = []
            for i in range(1,len(myEtudiantDatas)):
                etudiantData = myEtudiantDatas[i].split() # ['nom', '|', 'age', '|', 'sexe']
                etudiant = Exercice2.Etudiant(etudiantData[0],etudiantData[2],etudiantData[4])
                etudiantList.append(etudiant)

            return etudiantList

    #! a- Invitez l'utilisateur à entrer le nom, l'age et sexe de n etudiants via le console du System

    def getEtudiantData(self):

        print("\nGet Etudiant Data\n")

        numberEtudiant = int(input("Entrer le nombre étudiant : "))

        etudiantList = []

        for i in range(numberEtudiant):
            nom = str(input(f"Entrez le nom de l'élève numéro {i} : "))
            age = int(input(f"Entrez son age : "))
            sexe = str(input("Entrez son sexe (f/m) : "))

            etudiant = Exercice2.Etudiant(nom,age,sexe)
            etudiantList.append(etudiant)

        self.etudiantList = etudiantList

        return 0

    #! b- Enregistrez les informations de ses etudiants dans un fichier nommée etudiant.txt

    def storeDataInFile(self):

        print("\nStore Data in File\n")

        myEtudiantFile = open("Etudiant.txt", "w")
        myEtudiantFile.write(self.fileHeader)
        
        for etudiant in self.etudiantList:
            myEtudiantFile.write(etudiant.toString())

        myEtudiantFile.close()

        return 0

    #! c- filtrer les informations des etudiants de type feminin dans le fichier etudiant.txt et les transettre dans etudiants.feminin.txt
    #! d- filtrer les informations des etudiants de type masculin dans le fichier etudiant.txt et les transmettre dans etudiant.masculin.txt

    def filterDataInCorrectFile(self):

        print("\nFilter Data In File\n") 

        feminFile = open("Etudiant.fem.txt", "a")
        mascFile = open("Etudiant.masc.txt", "a")

        feminFile.write(self.fileHeader)
        mascFile.write(self.fileHeader)

        etudiantList = Exercice2.Etudiant.getAllEtudiants()

        for etudiant in etudiantList:
            if etudiant.sexe == "f":
                feminFile.write(etudiant.toString())
            elif etudiant.sexe == "m":
                mascFile.write(etudiant.toString())

        feminFile.close()
        mascFile.close()

        return 0

    def __init__(self) -> None:
        self.getEtudiantData()
        self.storeDataInFile()
        self.filterDataInCorrectFile()

Exercice2()
# FINISH : 08"55