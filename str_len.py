def longueur(x):                #on définit une focntion qui ca compter le nombre de caractère
    i = int(0)                  #on initie le compteur à 0
    for lettre in x:            #on commebce la boucle qui va compter le nombre de lettre
       i = i+1                  #on incrémente de 1 le compteur à chaque lettre
    print(i , "caractères")     #on affiche le nomvre de caractères

chaine = str(input("Entrez votre chaine de caractère : "))
longueur(chaine)