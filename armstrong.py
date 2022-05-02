chiffre = int(input("Quel est votre nombre ? : "))
sum = 0
n = len(str(chiffre))

temp = chiffre
while temp >0:
    digit = temp%10
    sum += digit ** n
    temp //=10
    
if chiffre == sum:
    print("Le nombre " , chiffre , " est Armstrong")
else:
    print("Le nombre " , chiffre , " n\'est pas Armstrong")