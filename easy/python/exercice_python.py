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