ventas = []


for i in range (4):
    fila = []

    for j in range(5):
        print(f"Ingrese el valor de la venta { i + 1} del mes {j + 1}:")
        fila.append(float(input()))

    ventas.append(fila) 

for i in range(4):
        total_productos = sum(ventas[i])
        print(f"El total de ventas del producto {i + 1} es: {total_productos}")

for j in range(5):
        total_semana = sum(ventas[i][j] for i in range(4))
        print(f"El total de ventas de la semana {j + 1} es: {total_semana}")
    

        