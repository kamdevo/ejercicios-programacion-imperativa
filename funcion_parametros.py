def nombre_funcion(nombre) :
    nombre = 'Don', nombre

    print('Hola', nombre)
    print('Función de parametros sin retorno')


def main():
    nombre = input('Ingrese el nombre')
    nombre_funcion(nombre)
    print('Tu nombre es', nombre)


main()