# programa 3-16 que determina que tipo de triangulo es, de acuerdo a sus numero de lados.
# Triángulo escaleno su tres lados tienen longitudes diferentes
# Triangulo isoceles tiene dos lados iguales y uno diferente también.
# Triangulo equilatero miden sus tres lados lo mismo.

lados = int (input("Ingresa cuantos lados iguales tiene el triangulo: "))

if lados == 0:
    print("Triangulo escaleno")
else:
    if lados == 2:
        print("Triangulo isoceles")
    else:
        if lados == 3:
            print("Triangulo equilatero")
        else:
            print("Dato fuera de rango, no es un triangulo")
