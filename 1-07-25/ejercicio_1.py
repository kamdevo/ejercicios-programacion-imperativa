array_numeros = []
suma = 0


for i in range(10):
    print(f"Ingrese el número # {i + 1}:")
    numero = int(input())
    suma += numero
    array_numeros.append(numero)

print("La suma de los números es:", suma)