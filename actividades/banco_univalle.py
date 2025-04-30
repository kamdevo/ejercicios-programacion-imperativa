import math

def solicitar_datos():
    print('Ingrese el monto de dinero a prestar: ')
    monto = int(input())
    print('Ingrese el tiempo de prestamo en meses: ')
    tiempo = int(input())

    return monto, tiempo

def calcular_interes(monto, tiempo):
    if monto > 3000000  :
        interes =  1.5/100
    elif 1500000 <= monto <= 3000000 and tiempo >= 12:
        interes = 1.7/100
    elif 1500000 <= monto <= 3000000 and tiempo < 12:
        interes =  1.9 / 100
    elif monto < 1500000 and tiempo >= 12:
        interes =  1.8/100
    elif monto < 1500000 and tiempo < 12:
        interes =  2.5/100
    
    return interes


def calcular_cuota_fija(monto, interes, tiempo):
    cuota = monto * interes * math.pow(1 + interes, tiempo) / (math.pow(1 + interes, tiempo) - 1)
    return cuota


def main():
    monto, tiempo = solicitar_datos()
    interes = calcular_interes(monto, tiempo)
    cuota = calcular_cuota_fija(monto, interes, tiempo)
    
    saldo = monto
    for i in range(tiempo):
        interes_mensual = saldo * interes
        saldo_final = (saldo - cuota) + interes_mensual
        print('Mes Saldo Interes Cuota Saldo final')
        print(f'{i+1} {math.trunc(saldo)} {math.trunc(interes_mensual)} {math.trunc(cuota)} {math.trunc(saldo_final)}')
        saldo = saldo_final



if __name__ == '__main__':
    main()