def conversion(distance):                               #fonction qui converti les miles en km
    km = float(distance * 1.6)                          #formule pour converti les miles en km
    km = str(km)                                        #on converti l'entier en chaine de caractère pour pouvoir l'afficher
    print("La distance en km est de : " + km)           #on affiche le résultat

mile = float(input("Quelle est la distance ? "))        #on demande la distance en km
conversion(mile)