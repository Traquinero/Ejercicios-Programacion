import datetime

def edad(anio_nac):
    hoy = datetime.datetime.today()
    return hoy.year - anio_nac

mi_edad = edad(1992)

print("Este año cumples", mi_edad, "años")

dato = type(0.05)
print(dato)



