# programa 3-11 para calcular el pago del recibo de luz de una persona
costo_kilowatts = 0.8
cargo_extra = 15
num_medidor = str (input("Dame el numero del medidor: "))
kilowatt = int (input("Dame la cantidad de kilowatts consumidos: "))
saldo_anterior = float (input("Dane el saldo anterior: "))

if saldo_anterior > 0:
    costo_total = (costo_kilowatts * kilowatt) + cargo_extra + saldo_anterior
    print("El costo total del medidor ", num_medidor, " es: ", costo_total)
else:
    costo_total = costo_kilowatts * kilowatt
    print("El costo total del medidor ", num_medidor, " es: ", costo_total)
