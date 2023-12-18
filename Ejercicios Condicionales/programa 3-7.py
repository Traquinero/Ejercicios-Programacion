# programa 3-7 calcular el area de un triangulo
base = float (input("Dame la longitud de la base: "))
altura = float (input("Dame la altura: "))
if base <=0 or altura <=0:
    print("La base o la altura o ambas son cero o negativos, no tiene caso hacer calculos con estos numeros")
else:
    area = base * altura / 2
    print("si la base mide ", base, " y la altura mide ", altura, " El area del triangulo es: ", area)
