# programa 3-14 para determinar el grado del acero inoxidable T1 y T2
T1 = float (input("Dame el valor T1: "))
T2 = float (input("Dame el valor T2: "))

if T1 > 0.95 and T2 > 0.75:
    print("El acero es de grado 1")
else:
    if T1 > 0.95 and T2 < 0.76:
        print("El acero es de grado 2")
    else:
        if T1 < 0.96:
            print("El acero es de grado 3")
