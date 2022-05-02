def listAlphabet():                                                     #fonction qui va afficher les lettres de l'alphabet
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    alphabet_inverse = alphabet[::-1]                                   #formule pour inverser le tableau qui contient les lettres
    return alphabet_inverse                                             #on renvoie le résultat
print(listAlphabet())