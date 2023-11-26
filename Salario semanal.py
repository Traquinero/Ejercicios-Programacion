htr = int(input("Dame las horas trabajadas: "))
pht = int(200)
if htr > 40:
    hte = int(htr - 40)
    print("Horas extras: ", hte, "hr")
    site = int(hte * pht * 1.5)
    st = int((pht * 40) + site)
    print("salario parcial tiempo extra: ", site, "pesos")
    print("Salario total: ", st, "pesos")
elif 0 < htr <= 40:
    stol = int(htr * pht)
    print("Salario total sin tienmpo extra: ", stol, "pesos")
