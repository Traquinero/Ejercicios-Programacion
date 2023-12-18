# programa 3-12 ¿Cual numero es mayor?
valor1 = float (input("Dame el primer numero: "))
valor2 = float (input("Dame el segundo numero: "))

if valor1 == valor2:
    print("No se puede determinar cual numero es mayor porque son iguales")
else:
    if valor1 > valor2:
        print("El primer numero ", valor1 , " es mayor al segundo ", valor2)
    else:
        print("El segundo numero ", valor2, " es mayor al primero ", valor1)