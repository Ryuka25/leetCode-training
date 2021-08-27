#!/usr/bin/env python

import math

def question1():
    
    # Ecrire un algorithme qui calcule la somme de n premiers entiers.

    def npremier(nombre:int)-> list:
        result = [1] # Le premier nombre premier est 1 est non pas 0
        for i in range(1,nombre):
            actual = i
            result.append(actual + (i+1))

        return result

    result = npremier(5)
    print(result)

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

def main():
    question5()
    return 0

if (__name__ == '__main__'):
    main()