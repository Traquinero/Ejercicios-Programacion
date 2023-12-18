# programa 3-2 calculo de la fuerza
masa = float(input("Dame la masa: "))
if masa <= 0:
    print("la masa es cero o negativo. no tiene caso hacer calculos con este numero")
else:
    acele = float(input("Dame la aceleración: "))
    fuerza = masa * acele
    print("Cuando la masa", masa , " y la aceleración ", acele, " la fuerza es ", fuerza)