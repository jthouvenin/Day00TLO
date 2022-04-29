def listAlphabet():
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    alphabet_inverse = alphabet[::-1]
    return alphabet_inverse
print(listAlphabet())