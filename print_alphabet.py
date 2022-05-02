def listAlphabet():                                           #fonction qui va chercher les lettres de l'alphabet
  return [chr(i) for i in range(ord('a'),ord('z')+1)]         #on renvoie les lettre de l'alphabet trié dans l'ordre
print(listAlphabet())