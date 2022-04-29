annee = int(input("Entrez l\'année : "))

if annee%4 !=0:
    print("L'annéee ", annee , "n'est pas bissextile")
else:
    if annee%100 == 0:
        if annee%400 == 0:
            print("L'année " , annee , "est bissextile")
        else:
            print("L'année ", annee , "n'est pas bissextile")
    else:
        print("L'année ", annee , "n'est pas bissextile")