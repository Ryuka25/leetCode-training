#!/usr/bin/env python

# INFO 160 - ALGORITHMES FONDAMENTAUX

def exo_1():

    # Exercice 1
    # écrire l'algorithe qd'affichage du plus grand de 2 nombres saisis au clavier.

    number1 = float(input("[?] Entrez une nombre : "))
    number2 = float(input("[?] Entrez une autre nombre : "))
    print(f"[*] The max betwenn {number1} and {number2} is {max(number1, number2)} !")
    
    return 0

def exo_2():

    # Exercice 2
    # écrire un algorithme qui propose un menu afficé à l'écran,
    # et qui, en fonction du choixx fait par l'utilisateur, 
    # effectue soit la somme, soit le produit, soit la moyenne de 2 nombres saisi.
    # Prévoir le cas où l'utilisateur a fait une erreur de saisie

    def operation(operateur:int, n1:float, n2: float):
        if (operateur == 1 ):
            return f"[*] La somme de {n1} et {n2} est {(n1+n2)}"
        elif (operateur == 2):
            return f"[*] Le produit de {n1} et {n2} est {(n1*n2)}"
        elif (operateur == 3):
            return f"[*] La moyenne de {n1} et {n2} est {(n1+n2)/2}"

    choose = True
    print("[*] Voici les actions disponnibles :\n\t1- Somme de deux nombres\n\t2- Produit de deux nombres\n\t3- Moyenne de deux nombres\n\t")
    while choose:
        operateur = int(input("[?] Vous voullez faire quelle action ? (123) > "))
        if (operateur in [1,2,3]):
            break
        else:
            print("[!] Veuillez entrez un nombre valide !")
            pass

    number1 = float(input("[?] Entrez une nombre : "))
    number2 = float(input("[?] Entrez une autre nombre : "))
    print(operation(operateur, number1, number2))

    return 0

def exo_3():

    # Exercice 3
    # Ecrire l'algorithme permettant d'afficher la table de multiplication selon la valeur saisie en entrée.

    def afficheTable(number:int):
        print("[*] Voici le table de multiplication du nombre {}".format(number))
        for i in range(0,11):
            print(f"\t{number} * {i} = {number*i}")

    number = int(input("[?] Entrez le nombre pour la table de multiplication : "))
    afficheTable(number)

    return 0

def exo_4():

    # Exercice 4
    # Ecrire une fonction permettant d'encrypter un code alphanumérique de 5 caractères (Ex: A45Qn) saisie par l'utilisateur.
    # Les règles d'encryptages sont les suivants.
    #
    #   1- Les chiffrez sont transformés par ses valeurs précédentes (Ex: 5 vaut 4)
    #   2- Les lettrse minuscules sont transformés par une lettre majuscule de la valeur suivante (Ex: m vaut N)
    #   3- Les lettres majuscules sont transformés en '*'
    #
    # estMaj(variable) qui retourne VRAI si une caractère est majuscule
    # estMin(variable) qui retourne VRAI si une caractère est minuscule

    def estMaj(char:str) -> bool:
        if (char == char.upper()):
            return True
        else:
            return False

    def estMin(char:str) -> bool:
        if (char == char.lower()):
            return True
        else:
            return False

    def estNum(char:str) -> bool:
        try:
            int(char)
            return True
        except:
            return False
        

    def encryption(char) -> str :
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        if (estNum(char)):
            char = int(char)
            return f"{char+1}"

        elif (estMaj(char)):
            
            return "*"

        elif (estMin(char)):
            decIndex = alphabet.find(char)
            encChar = alphabet[(decIndex+1)%26].upper()
            
            return encChar

        else:

            return char

    decCode = str(input("[?] Entrez les caractères à encrypter : "))
    encCode = ""
    for char in decCode:
        encCode += encryption(char)
    
    print(f"[*] {decCode} encrypté dévient {encCode}")

    return 0

def main():
    print("\n[!] Ceci est une réplication du partie 2 de l'examen INFO_160 en version python ! ")
    print("[*] Voici les exercices proposées:\n\t1 - exo_1\n\t2 - exo_2\n\t3 - exo_3\n\t4 - exo_4\n\n\t99 - quit")
    choose = True
    while choose:
        exo = int(input("[?] Vous voullez testez quelles exercices ? (1234) > "))
        if (exo in [1,2,3,4,99]):
            if (exo == 1):
                exo_1()
            elif (exo == 2):
                exo_2()
            elif (exo == 3):
                exo_3()
            elif (exo == 4):
                exo_4()
            elif (exo == 99):
                break
        else:
            print("[!] Choisissez un nombre corrècte !")
            pass

    
    
    return 0

if (__name__ =='__main__'):
    main()