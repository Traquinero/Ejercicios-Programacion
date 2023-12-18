# programa 3-17 que determina que tipo de triangulo es, de acuerdo a los valores de los lados
# Triángulo escaleno su tres lados tienen longitudes diferentes
# Triangulo isoceles tiene dos lados iguales y uno diferente también.
# Triangulo equilatero miden sus tres lados lo mismo.

lado1 = int (input("Ingresa lado1: "))
lado2 = int (input("Ingresa lado2: "))
lado3 = int (input("Ingresa lado3: "))

lista = [lado1,lado2,lado3]

if lado1 == lado2 == lado3:
    print(" \n Es un triangulo equilatero")
else:
    lista.sort()
    # print("Lista ordenada",lista)
    if lista[1] == lista[2] or lista[0]==lista[2] or lista[0]==lista[1] :
        print(" \n Es un triangulo isoceles")
    else:
        print(" \n Es un triangulo escaleno")

	#    l1	l2	l3
    # 0	 0	0	0
    # 1	 0	0	1
    # 2	 0	1	0
    # 3	 0	1	1
    # 4	 1	0	0
    # 5	 1	0	1
    # 6	 1	1	0
    # 7	 1	1	1
