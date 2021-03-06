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

def volumePara(largeur,hauteur,profondeur):
    """
    Écrivez un programme qui calcule le volume d’un parallélépipède rectangle
    dont sont fournis au départ la largeur, la hauteur et la profondeur.
    """
    result = (largeur*hauteur*profondeur)

    return result

def timeConverter(seconde:int):
    """
    Écrivez un programme qui convertit un nombre entier de secondes
    fourni au départ en un nombre d’années, de mois, de jours, de minutes et de secondes
    (utilisez l’opérateur modulo : %).
    """
    #     annees,     resteAnnees     = seconde//31104000,    (seconde%31104000)     # 31104000s = 259200h   = 360j  = 12mois = 1an
    #     mois,       resteMois       = resteAnnees//2592000, (resteAnnees%2592000)  # 2592000s  = 720h      = 30j   = 1mois
    #     jours,      resteJours      = resteMois//86400,     (resteMois%86400)      # 86400s    = 24h       = 1j
    #     heures,     resteHeures     = resteJours//3600,     (resteJours%3600)      # 3600s     = 1h
    #     minutes,    resteMinutes    = resteHeures//60,      (resteHeures%60)       # 60s
    #     secondes                    = resteMinutes                                 #

    #     result = [annees, mois, jours, heures, minutes, secondes]

    #     return result
    pass

def correction_timeConverter(nsd):
    """
    Écrivez un programme qui convertit un nombre entier de secondes
    fourni au départ en un nombre d’années, de mois, de jours, de minutes et de secondes
    (utilisez l’opérateur modulo : %).
    """
    #     nsph = 3600                 # nbSecondeParHeure
    #     nspj = nsph * 24            # nbSecondeParJour
    #     nspm = nspj * 30            # nbSecondeParMoi
    #     nspa = nspj * 365           # nbSecondeParAn

    #     na = nsd // nspa
    #     nsr = nsd % nspa 

    #     return f"seconde = {nsd} vaut {nsr} et {na} an(s)"
    pass

# print(correction_timeConverter(3656565621))

def tableAsterix(base=7, multiple=3, start=0, stop=20):
    """
    Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7, en
    signalant au passage (à l’aide d’une astérisque) ceux qui sont des multiples de 3.
    """
    result=[]

    for i in range(start, stop):
        temp = f"{(i*base)}"
        if ((i*base)%multiple==0):
            temp = f"{temp}*"
        result.append(temp)

    return result

def tableSeulement(base=13, multiple=7, start=0, stop=50):
    """
    Écrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13,
    mais n’affiche que ceux qui sont des multiples de 7.
    """
    result = []

    for i in range(start, stop):
        temp = i*base
        if (temp%multiple == 0):
            result.append(temp)
    
    return result

def pyramideAsterix(string="*",start=0,stop=7):
    """
    Écrivez un programme qui affiche la suite de symboles suivante :

    *
    **
    ***
    ****
    *****
    ******
    *******
    """

    result = ""

    for i in range(start, stop):
        temp = ""
        for i in range(i+1):
            temp += string
        result = f"{result}\n{temp}"

    return result

def convertisseurRadDeg(angleRad):
    """
    Écrivez un programme qui convertisse en radians 
    un angle fourni au départ en degrés,minutes,secondes.
    """
    angle = {
        "radian":0.01745,
        "degre":1.0,
        "minute":60,
        "seconde": 3600
    }

    #     angleDegre= (angleRad//angle["radian"])

    #     angleMinute, reste_angleMinute = (angleRad*angle["minute"]//angle["radian"])//60, (angleRad*angle["minute"]//angle["radian"])%60
    #     angleSeconde = reste_angleMinute
        
    #     return [angleRad, angleDegre,angleMinute, angleSeconde]
    pass

# print(convertisseurRadDeg(1))