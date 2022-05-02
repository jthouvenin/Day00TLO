def tri_insertion(L):                                   #On définit la fonction de tri
    N = len(L)                                          #longueur du tableau
    for n in range(1,N):                                #boucle qui va parcourir chaque élément du tableau
        cle = L[n]                                      #la clé est l'élément à insérer
        j = n-1
        while j>=0 and L[j] > cle:                      #la boucle permet d'insérer la clé et de faire le tri en fonction des éléments
            L[j+1] = L[j] # decalage
            j = j-1
        L[j+1] = cle

import random
liste = []
for k in range(15):                                     #génération aléatoire des 15 entiers entre 0 et 100 dans le tableau
    liste.append(random.randint(0,100))
tri_insertion(liste)                                    #on appelle la fonction qui va faire le tri dans le tableau                       

print(liste)