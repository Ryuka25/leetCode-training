#!/usr/bin/env python

import math
from typing import Counter

def question1():
    
    # Ecrire un algorithme qui calcule la somme de n premiers entiers.

    def test_nombre_premier(nombre:int)->bool:
        if (nombre==1):
            result= True
        else:
            for i in range(2,nombre+1):
                if (nombre%i==0):
                    if (nombre==i):
                        result=True
                    else: 
                        result=False
                    break # le premier test suffit pour le test
        
        return result

    def n_nombre_premier(limit:int)-> list:
        result=[]

        i=1
        while (len(result) < limit):
            if (test_nombre_premier(i)):
                result.append(i)

            i+=1

        return result

    result = (sum(n_nombre_premier(5)))
    print(f"sum({n_nombre_premier(5)} = {result}")

def question2():

    # Ecrire un algorithme qui calcule le factoriel de n.

    math.factorial(4)

    def factoriel(nombre:int)->int:
        if (nombre == 0):
            result = 1
        else:
            result = nombre * factoriel(nombre-1)

        return result
    
    result = factoriel(4)
    print(result)


def question3():

    # Ecrire un algorithme qui calcule le monôme pow(X,n).

    math.pow(2,3) # 2**3 == pow(2,3)

    def puissance(nombre:float, puissance:int)->float:
        original = nombre
        for i in range(puissance-1):
            nombre = original * nombre

        return nombre

    result = puissance(2,3)
    print(result)


def question4():

    # Ecrire un algorithme qui calcule le factoriel de 𝐶 𝑝𝑛 .

    math.comb(4,2)

    def combinaison(n:int,p:int,)->float:
        # math.comb(n,p) # n:items dans le sac p:items à piocher
        result = (math.factorial(n)) / (math.factorial(p)*(math.factorial(n-p)))
        
        return result

    result=combinaison(4,2)
    print(result)

def question5():

    # Ecrire un algorithme pour trouver le terme général de la suite:
    # 𝑈 𝑛 = 2 · 𝑈 𝑛−1 + 1, où
    # 𝑈 0 = 1

    def U(n:int)->int:
        result=(0)
        if (n == 0):
            result=(1)
        else:
            result=((2*U(n-1))+1)
        
        return result

    result = U(1)
    print(result)

def question6():

    # Ecrire un algorithme pour calculer la suite de Fibonacci:
    # 𝑈 𝑛 =· 𝑈 𝑛−1 + 𝑈 𝑛−2 + 1, où
    # 𝑈 0 = 𝑈 1 = 1.

    def U(n:int)->int:
        result=(0)                      # Initialisation du résultat
        if (n==0 or n==1):
            result=(1)
        else:
            result=result+(U(n-1)+U(n-2)+1)

        return result

    result=U(2)
    print(result)
    
# def question7():

#     # Ecrire un algorithme pour savoir si un nombre appartient aux suite de Fibonacci ou non

#     def test_Fibonnaci(nombre:int)->bool:
        
#         while (nombre <= U(i)):
#         return result

def main():
    question6()
    return 0

if (__name__ == '__main__'):
    main()