# programa 3-4 calcular la velocidad final

from math import sqrt

altura = float(input("Dame la altura: "))
if altura <=0:
    print("La altura es cero o negativa, no tiene caso hacer calculos con este numero")
else:
    vf = sqrt (2 * 9.8 * altura)
    print("Cuando la altura es ", altura, " metros, la velocidad al momento del impacto es ", vf, " m/seg")

