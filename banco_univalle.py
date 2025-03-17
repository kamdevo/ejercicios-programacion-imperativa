def solicitar_datos():
    print('Ingrese el monto de dinero a prestar: ')
    monto = float(input())
    print('Ingrese el tiempo de prestamo en meses: ')
    tiempo = int(input())

    return monto, tiempo

def calcular_interes(monto, tiempo):
    if monto > 3000000  :
        interes = 1.5
    elif 1500000 <= monto <= 3000000 and tiempo >= 12:
        interes = 1.7
    elif 1500000 <= monto <= 3000000 and tiempo < 12:
        interes = 1.9
    elif monto < 1500000 and tiempo >= 12:
        interes = 1.8
    elif monto < 1500000 and tiempo < 12:
        interes: 2.5


def calcular_cuota_fija(monto, interes):
    cuota = monto * interes * math.pow(1 + interes, tiempo) / (math.pow(1 + interes, tiempo) - 1)
