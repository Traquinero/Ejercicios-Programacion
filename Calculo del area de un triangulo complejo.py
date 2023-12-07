# programa que los indica a travez de sus tres lados si es posible o no formar un triangulo.

from math import sqrt

lista = [31, 45, 22]

lado1 = float(lista[0])
print("Lado1: ", lado1, "Cm")
lado2 = float(lista[1])
print("Lado2: ", lado2, "Cm")
lado3 = float(lista[2])
print("Lado3: ", lado3, "Cm")

# esto imprime la lista NO ordenada
print("Lista de lados desordenada: ", lista)

# Ordenemos la lista
lista.sort()

# aquí tendremos la lista ordenada
print("Lista de lados Ordenada: ", lista)

suma = lista[0] + lista[1]
if suma > lista[2]:
    print("Se puede formar un triangulo")
    lados = (lista[0] + lista[1] + lista[2]) / 2
    area = sqrt(lados*(lados-lado1)*(lados-lado2)*(lados-lado3))
    print("El area del triangulo es: ", area, "Cm2")
else:
    print("No se puede formar un triangulo")