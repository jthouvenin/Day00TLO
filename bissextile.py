annee = int(input("Entrez l\'année : "))                                        #on demande l'année

if annee%4 !=0:                                                                 #test si l'année est divisible par 4
    print("L'annéee ", annee , "n'est pas bissextile")
else:
    if annee%100 == 0:                                                          #test si l'année est divisible par 100 (en + de 4)
        if annee%400 == 0:                                                      #test si l'année esr divisible par 400 (en + des 2 autres conditions)
            print("L'année " , annee , "est bissextile")
        else:
            print("L'année ", annee , "n'est pas bissextile")
    else:
        print("L'année ", annee , "n'est pas bissextile")