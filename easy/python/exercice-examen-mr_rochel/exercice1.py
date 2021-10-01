#! /usr/bin/env python

"""
Soit la liste suivante :
list1 = [19,4,13,18,24,39,6,1,79,100]
list2 = [1,2,9,18,6,3,29,31,42,0]

a) créez un programme en python capable de ordonner la liste list1 de manière croissante.
=> Résultat : [1,4,6,13,18,19,24,39,79,100]

b) créez un programme en python capable de ordonner la liste list2 de manière décroissante
=> Résultat : [42,31,29,18,9,6,2,1,0]

"""

# START : 07"30

#! Déclaration des list:

list1 = [19,4,13,18,24,39,6,1,79,100]
list2 = [1,2,9,18,6,3,29,31,42,0]

#! a) créez un programme en python capable de ordonner la liste list1 de manière croissante.

def sortListASC(unsortedList: list):
    for i in range(len(unsortedList)):
        for j in range(i, len(unsortedList)):
            if unsortedList[i] > unsortedList[j]:
                unsortedList[i], unsortedList[j] = unsortedList[j], unsortedList[i]

    return unsortedList

print(sortListASC(list1));

#! b) créez un programme en python capable de ordonner la liste list2 de manière décroissante

def sortListDESC(unsortedList: list):
    for i in range(len(unsortedList)):
        for j in range(i, len(unsortedList)):
            if unsortedList[i] < unsortedList[j]:
                unsortedList[i], unsortedList[j] = unsortedList[j], unsortedList[i]

    return unsortedList

print(sortListDESC(list2));

#! Built-In Function

# print(sorted(list1, reverse=False))
# print(list1.sort())
# print(sorted(list2, reverse=True))
# print(list2.sort(reverse=True))

# FINISH : 08"05