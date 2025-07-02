
lista_reales = []


for i in range(15):
    print(f"Ingrese el número # {i + 1}:")

    lista_reales.append(float(input()))

    if i == 0:
        menor = lista_reales[0]
        mayor = lista_reales[0]
    
    if lista_reales[i] < menor:
        menor = lista_reales[i]

    if lista_reales[i] > mayor:
        mayor = lista_reales[i]

print("El número menor es:", menor)
print("El número mayor es:", mayor)