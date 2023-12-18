# programa 3-1bis
matricula = str (input("Dame la matricula: "))
nombre = str (input("Dame el nombre del alumno: "))
calf1 = float (input("Dame la primera calificación: "))
calf2 = float(input("Dame la segunda calificación: "))
prom = (calf1 + calf2)/2
if prom >= 7:
    situacion = str("aprobado")
else:
    situacion = str("reprobado")
print("El alumno con matricula ", matricula, " se llama ", nombre)
print("Tiene promedio ", prom , "y está" , situacion)