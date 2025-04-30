#Programa: vena.py
#Propósito: Calcular valor de venta
# 27/02/2025
#Autor: Juan Camilo Morales

#Definición e inicialización de variables
venta = 0.0
descuento = 0.0
neto_pagar = 0.0

#Datos de entrada
venta = float(input('Ingrese el valor de venta\n'))

if venta > 500000:
    descuento = venta * 0.10
else:
    descuento = venta * 0.05

neto_pagar = venta - descuento

print('El valor de venta es: ',venta)
print('El descueto es: ',descuento)
print('El valor neto a pagar es: ', neto_pagar)