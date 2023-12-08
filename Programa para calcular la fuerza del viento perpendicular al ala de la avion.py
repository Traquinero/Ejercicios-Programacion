# Programa para calcular la fuerza del viento perpendicular al ala de la avion.
# Un avion que se encuentra a una altura de 10000 pies y a 150 millas por hora, desarrolla velocidades relativas
# con respecto al viento de 300 millas por hora en la parte superior del ala y 80 millas por hora debajo de la ala.
# Si el area del ala es de 160 pies^2.
# ¿Cual sera la fuerza perpendicular a ella?
# Concidere la densidad a 10000 pies de altura es p= 0.001756 slugs/pies3
# la formula es: fuerza = A * (1 / 2) * p ( V1^2 - V2^2)
# Donde:
# A es el area de el ala del avion -> 160 pis^2
# p es la densidad a 10000 pies es -> 0.00175 slugs/pies^3
# V1 es la velocidad relativa del viento en la parte superior del ala -> 300 millas por hora
# V2 es la velocidad relativa del viento en la parte inferior del ala -> 80 millas por hora
# El factor que debe usarse para convertir las millas por horas a pies por segundo es 44 / 30

densidad = 0.00175
area = float (input("Dame el area del ala del avion pies^2: "))
v1 = float (input("Dame la velocidad relativa del viento en la parte superior del ala millas/hora: "))
v2 = float (input("Dame la velocidad relativa del viento en la parte inferior del ala millas/hora: "))

v1 = (44 / 30) * v1
v2 = (44 / 30) * v2
fuerza = area * (0.5) * (densidad) * (v1**2 - v2**2)
print("La fuerza del viento perpendicular al ala del avion es de: ", fuerza, "N")