# programa 3-15 que calcula los pagos de los recibos de luz con base en las siguientes tarifas
KWH_14 = 30
KWH_51 = 0.5
KWH_65 = 0.25
KWH_CONSUMIDOS = int (input("Dame los kilos Watts consumidos: "))
if KWH_CONSUMIDOS <= 14:
    PAGO = KWH_CONSUMIDOS*KWH_14
    print("Pago a realizar: ", PAGO)
else:
    if KWH_CONSUMIDOS >=15 and KWH_CONSUMIDOS <=51:
        PAGO = KWH_CONSUMIDOS * KWH_51
        print("Pago a realizar: ", PAGO)
    else:
        if KWH_CONSUMIDOS >=52 and KWH_CONSUMIDOS <=65:
            PAGO = KWH_CONSUMIDOS * KWH_65
            print("Pago a realizar: ", PAGO)
        else:
            print("Exceso de kilowass")
