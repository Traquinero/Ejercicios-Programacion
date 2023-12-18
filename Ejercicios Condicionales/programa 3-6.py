# programa 3-6 calcula el area de un circulo
r = float (input("Dame la longitud del radio del circulo: "))
if r <=0:
    print("El radio es cero o negativo, no tiene caso hacer cálculos con este numero")
else:
    A = 3.1416 * r**2
    print("Si el radio mide" , r , " el area del circulo es ", A)
