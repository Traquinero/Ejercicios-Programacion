# programa 3-3 convierte de pies a metros
pies = float (input("Dame los pies: "))
if pies <=0:
    print("La cantidad en pies es cero o negativo, no tiene caso hacer calculos con este numero")
else:
    metros = pies * 0.3048
    print("Los ", pies, " pies equivalen a ", metros, " metros")
