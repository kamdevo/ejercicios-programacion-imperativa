definitivas = []
estudiantes = []

n = 5

for i in range(n):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota1 = float(input("Ingrese la nota de parcial 1: "))
    nota2 = float(input("Ingrese la nota de parcial 2: "))
    nota3 = float(input("Ingrese la nota de laboratorios: "))
    final = (nota1*0.4 + nota2 * 0.35 + nota3 * 0.25)
    estudiantes.append(nombre)
    definitivas[i] = final
    perint('Nota definitiva: ', definitivas[i])
    sumaDefinitivas += definitivas[i]

    

    definitivas.pop(0) # eliminar elemento en posicion 0
    definitivas.insert(0, final) # insertar elemento en posicion 0
    definitivas.remove(0) # eliminar elemento en posicion 0
