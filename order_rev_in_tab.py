def tri_insertion(L):                                           #fichier idetique à order_int_tab.py
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and L[j] > cle:
            L[j+1] = L[j] # decalage
            j = j-1
        L[j+1] = cle

import random
liste = []
for k in range(15):
    liste.append(random.randint(0,100))
tri_insertion(liste)

liste_inverse = liste[::-1]                                     #fonction qui permet d'inverser le tableau (donc d'afficher en ordre décroissant)

print(liste_inverse)