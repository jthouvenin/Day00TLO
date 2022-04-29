def conversion(distance):
    km = float(distance * 1.6) 
    km = str(km)
    print("La distance en km est de : " + km)

mile = float(input("Quelle est la distance ? "))
conversion(mile)