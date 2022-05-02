chiffre1 = int(input("Quel est le premier nombre : "))                          #on demande le premier nombre
chiffre2 = int(input("Quel est le second nombre : "))                           #on demande le 2e nombre
operation = str(input("Quelle est l'opération demandée (+ - / *) : "))          #on demande l'opération

if operation == "+":                                                            #si l'opération est une addition
    print(chiffre1 , " + " , chiffre2 , " = " , chiffre1+chiffre2)

if operation == "-":                                                            #si l'opération est une soustraction
    print(chiffre1 , " - " , chiffre2 , " = " , chiffre1-chiffre2)

if operation == "*":                                                            #si l'opération est une multiplication
    print(chiffre1 , " * " , chiffre2 , " = " , chiffre1*chiffre2)

if operation == "/":                                                            #si l'opération est une division
    print(chiffre1 , " / " , chiffre2 , " = " , chiffre1/chiffre2)