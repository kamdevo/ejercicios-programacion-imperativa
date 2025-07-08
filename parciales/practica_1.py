#programa de practica

facturas = [
  [245698, 3256, 30],
  [24568, 4432, 10],
  [456987, 2045, 2],
  [456987, 1003, 5],
  [324561 , 4567, 25]
]

productos = [
    [1003, "Vaso Cristal", 5466 ],
    [2045, "Jabón Barrigón", 2365 ],
    [3256, "Café Colombia", 365],
    [3367, "Arroz Grande",283 ],
    [4432 , "Aceite Sol",1524 ],
    [4567, "Azúcar Morena ", 2300]
]



# La tienda Univalle tiene registrado en una matriz (facturas), las facturas generadas
# en su proceso de venta, cada fila tiene el código del producto vendido para dicha
# facturas y la cantidad de artículos vendidos de éstos.
# Así mismo tiene almacenado en una matriz (productos), los datos correspondientes a
# cada producto (Código, Nombre Producto y Precio Unitario).
# Se requiere construir una función en Python que permita desplegar el siguiente
# Listado:


def listar_productos(productos, facturas):
  print("# de factura | Código producto | Nombre de producto | Cantidad | Precio unitario | Total ")
  for factura in facturas:
    for producto in productos:
      if producto[0] == factura[1]:
        numero_factura = factura[0]
        codigo_producto = producto[0]
        nombre_producto = producto[1]
        precio_unitario = producto[2]
        cantidad_producto = factura[2]
        total_producto = precio_unitario * cantidad_producto
        print(f"{numero_factura:<11}{codigo_producto:<17}{nombre_producto:<20}{cantidad_producto:<9}{precio_unitario:<16}{total_producto}")
        break

listar_productos(productos, facturas)
        