#Programa: vena.py
#Propósito: Calcular valor de venta
# 27/02/2025
#Autor: Juan Camilo Morales

#Definición e inicialización de variables
venta = 0.0
descuento = 0.0
neto_pagar = 0.0
forma_pago = 0

#Datos de entrada
venta = float(input('Ingrese el valor de venta\n'))
forma_pago = int(input('Ingrese la forma de pago\n 1. Efectivo\n 2. Cheque\n 3. Tarjeta Debito\n 4. Tarjeta crédito.\n 5. Crédito\n'))

match forma_pago:
    case 1: 
        descuento = venta * 0.20
    case 2:
        descuento = venta * 0.15
    case 3:
        descuento = venta * 0.10
    case 4:
        descuento = venta * 0.05
    case 5:
        descuento = 0
    case _:
        print('Opción no valida')


neto_pagar = venta - descuento

print('El valor de venta es: ',venta)
print('El descueto es: ',descuento)
print('El valor neto a pagar es: ', neto_pagar)