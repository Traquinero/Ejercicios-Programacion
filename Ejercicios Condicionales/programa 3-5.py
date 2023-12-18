# programa 3-5 calcular el area de un cuadrado
lado = float(input("Dame la longitud del lado: "))
if lado <=0:
    print("El lado es cero o negativo, no tiene caso hacer calculos con este numero:")
else:
    area = lado * lado
    print("Si el lado es " , lado , "el area del cuadrado es ", area , " m2")
