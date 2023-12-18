# programa 3-1 determina si el alumno paso la materia
parcial1 =  float(input("Dame la primer calificación: "))
parcial2 =  float(input("Dame la segunda calificación: "))
prom = (parcial1 + parcial2) / 2
print(prom)
if prom >= 7:
    print("El alumno está aprobado")
else:
    print("El alumno está reprobado")
