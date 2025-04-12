codigo = -1
total_factura = 0
total_producto = 0

while codigo != 0:
    codigo = int(input("Digite el código: "))

    if codigo != 0:
        cantidad = int(input("Digite la cantidad de productos: "))
        precio_unitario = int(input("Digite el precio unitario: "))
        total_producto = cantidad * precio_unitario
        total_factura = total_factura + total_producto
        print(f'El total del producto es: {total_producto}')

    
print(f'El total de la factura es: {total_factura}')