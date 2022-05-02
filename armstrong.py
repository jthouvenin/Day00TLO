chiffre = int(input("Quel est votre nombre ? : "))                      #on demande le nombre
sum = 0                                                                 #on défnit la variable sum à 0
n = len(str(chiffre))                                                   #n définit le nombre de chiffre du nombre

temp = chiffre                                                          #variable temp pour stocker temporairement le nombre de chiffre
while temp >0:                                                          #début de la boucle
    digit = temp%10                                                     
    sum += digit ** n
    temp //=10
    
if chiffre == sum:
    print("Le nombre " , chiffre , " est Armstrong")
else:
    print("Le nombre " , chiffre , " n\'est pas Armstrong")