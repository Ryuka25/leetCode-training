#!/usr/bin/env python

import math
from typing import Counter

class question1:
    
    # Ecrire un algorithme qui calcule la somme de n premiers entiers.

    def __init__(self,number) -> None:
        self.number=number
        self.result = (sum(self.n_nombre_premier(self.number)))

    def test_nombre_premier(self, nombre:int)->bool:
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

    def n_nombre_premier(self,limit:int)-> list:
        result=[]

        i=1
        while (len(result) < limit):
            if (self.test_nombre_premier(i)):
                result.append(i)

            i+=1

        return result

    def show(self):

        # show(number)
        # number = affichier les  {number} premier(s) nombre premier

        print(f"sum({self.n_nombre_premier(self.number)}) = '{self.result}'")

class question2:

    # Ecrire un algorithme qui calcule le factoriel de n.
    def __init__(self,number) -> None:
        self.number=number
        self.result=self.factoriel(self.number)

    def factoriel(self, nombre:int)->int:
        if (nombre == 0):
            result = 1
        else:
            result = nombre * self.factoriel(nombre-1)

        return result
    
    def show(self):
        
        # math.factorial()

        print(f"factoriel({self.number}) = '{self.result}'")

class question3:

    # Ecrire un algorithme qui calcule le monôme pow(X,n).

    def __init__(self,nombre,nb_puissance) -> None:
        self.nombre=nombre
        self.nb_puissance=nb_puissance
        self.result= self.puissance(self.nombre,self.nb_puissance)


    def puissance(self, nombre:float, nb_puissance:int)->float:
        original = nombre
        for i in range(nb_puissance-1):
            nombre = original * nombre

        return nombre

    def show(self):

        # math.pow(2,3) # 2**3 == pow(2,3)

        print(f"puissance({self.nombre},{self.nb_puissance}) = '{self.result}'")

class question4:

    # Ecrire un algorithme qui calcule le factoriel de 𝐶 𝑝𝑛 .
    
    def __init__(self,n,p) -> None:
        self.n=n
        self.p=p
        self.result=self.combinaison(self.n,self.p)

    def combinaison(self, n:int,p:int,)->float:

        # math.comb(n,p) # n:items dans le sac p:items à piocher

        result = (math.factorial(n)) / (math.factorial(p)*(math.factorial(n-p)))
        
        return result

    def show(self):

        # math.comb(4,2)

        print(f"combinaison({self.n},{self.p}) = '{self.result}'")

class question5:

    # Ecrire un algorithme pour trouver le terme général de la suite:
    # 𝑈 𝑛 = 2 · 𝑈 𝑛−1 + 1, où
    # 𝑈 0 = 1

    def __init__(self,number:int)->None:
        self.number=number
        self.result=self.U(self.number)

    def U(self, n:int)->int:
        result=(0)
        if (n == 0):
            result=(1)
        else:
            result=((2*self.U(n-1))+1)
        
        return result

    def show(self):
        print(f"U({self.number}) = '{self.result}'")

class question6():

    # Ecrire un algorithme pour calculer la suite de Fibonacci:
    # 𝑈 𝑛 =· 𝑈 𝑛−1 + 𝑈 𝑛−2 + 1, où
    # 𝑈 0 = 𝑈 1 = 1.
    
    def __init__(self,number) -> None:
        self.number=number
        self.result=self.U(self.number)

    def U(self, n:int)->int:
        result=(0)                      # Initialisation du résultat
        if (n==0 or n==1):
            result=(1)
        else:
            result=result+(self.U(n-1)+self.U(n-2)+1)

        return result

    def show(self):
        print(f"U({self.number}) = '{self.result}'")


class question7():

    # Ecrire un algorithme pour savoir si un nombre appartient aux suite de Fibonacci ou non
    
    def __init__(self,number:int) -> None:
        self.number=number
        self.result=(self.test_Fibonnaci(self.number))

    def test_Fibonnaci(self,nombre:int)->bool:
        
        # TODO: @Ryuka25 -> Vérifier cette fonction
        
        i = 0
        result=False                                    # Initialisation du result
        while (nombre <= question6(i).result):
            if (nombre == question6(i).result):
                result=True

            i+=1

        return result

    def show(self):
        print(f"test_Fibonnaci({self.number}) = '{self.result}'")

def main():

    question1(2).show()
    question2(4).show()
    question3(2,3).show()
    question4(4,2).show()
    question5(3).show()
    question6(4).show()
    question7(9).show()

    return 0

if (__name__ == '__main__'):
    main()