# Calcular el área de un cuadrado
# El area de un cuadrado es la multiplicación de sus tres lados
l = float(input("Dame el lado del cuadrado: "))
area = l * l
print("El area del cuadrado es: ", area, "Cm2")

# Calcular el area de un circulo
# El area de un circulo se calcula por pi por el radio al cuadrado

radio = float(input("Dame el radio del circulo: "))
pi = 3.1416
areac = pi * (radio)**2
print("El area del circulo es: ", areac, "Cm2")

# Calcular el area de un triangulo
# El area de un triangulo se calcula multiplicando la base por la altura sobre dos

base = float(input("Dane la base: "))
altura = float(input("Dame la altura: "))
aret = (base * altura) / 2
print("El area del triangulo es: ", aret, "Cm2")