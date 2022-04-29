chiffre1 = int(input("Quel est le premier nombre : "))
chiffre2 = int(input("Quel est le second nombre : "))
operation = str(input("Quelle est l'opération demandée (+ - / *) : "))

if operation == "+":
    print(chiffre1 , " + " , chiffre2 , " = " , chiffre1+chiffre2)

if operation == "-":
    print(chiffre1 , " - " , chiffre2 , " = " , chiffre1-chiffre2)

if operation == "*":
    print(chiffre1 , " * " , chiffre2 , " = " , chiffre1*chiffre2)

if operation == "/":
    print(chiffre1 , " / " , chiffre2 , " = " , chiffre1/chiffre2)