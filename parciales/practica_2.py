# 3. (40%) La Cadena de almacenes “calza Algoritmia” cuenta con 5 puntos de venta en la ciudad, en donde se
# venden 4 referencias de zapatos. Para almacenar la cantidad de zapatos vendidos de cada referencia en cada
# punto de venta, se cuenta con una matriz (ventas[4][5]) de tipo entero, donde las filas representan las
# referencias de zapatos, y las columnas representan los puntos de venta.

import random

ventas = [[random.randint(1,20) for y in range(5)] for x in range(4)]




def mostras_datos(ventas):
  total_vendidos = 0
  for i in range (len(ventas)):
    for j in range (len(ventas[i])):
      total_vendidos += ventas[i][j]

  print(f"El total de zapatos vendidos es: {total_vendidos}")


def main():
  print(ventas)
  mostras_datos(ventas) 

main()


