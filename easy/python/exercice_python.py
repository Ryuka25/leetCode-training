#!/usr/bin/python
# -*- conding:utf-8 -*-
#
# Cette script est une réceuille des solutions perso s
# des exercices du livre apprendre_python3_5.pdf

def tableMultiplication(base:int,start:int=0,stop:int=10):
    """
    Écrivez un programme qui affiche les 20 premiers termes
    de la table de multiplication par {base}.
    """
    result = f"Table de multiplication de {base}:"
    for i in range((start),(stop+1)): 
        result += f"\n\t{base} * {i}\t= {base*i}"
    
    return result

def tableConversion(start:float,end:float):
    """
    Écrivez un programme qui affiche une table de conversion de sommes d’argent 
    exprimées en euros, en dollars canadiens.
    La progression des sommes de la table sera « géométrique »
    """

    result = []
    for i in range(start,end):
        result.append(f"{i} euro(s) = {i*1.65:.2f} dollar(s)")

    return result

def triplement():
    """
    Écrivez un programme qui affiche une suite de 12 nombres
    dont chaque terme soit égal au triple du terme précédent.
    """

    def U(n):
        if (n==0):
            result = 1
        else:
            result = U(n-1)*3
        
        return result
    
    result = []
    for i in range(12):
        result.append(U(i))

    return result