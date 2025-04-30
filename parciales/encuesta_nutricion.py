porciones_semanales = 0
tipo_dieta = 0
total_personas = 0
opc = 's'
grupo_personas_1 = 0
grupo_personas_2 = 0



def ingresarDatos():
    global porciones_semanales, tipo_dieta
    
    print('¿Cuántas porciones de fruta y verdura consume semanalmente?')
    print('1. Menos de cinco porciones.')
    print('2. Entre 5 y 10 porciones.')
    print('3. Más de 10 porciones.')
    porciones_semanales = int(input(''))

    if validarDatoPorciones(porciones_semanales) == False:
        print('Error. Opción invalida, digite un código entre el 1 y el 3.')
        porciones_semanales = int(input(''))

    print('¿Cuál es su tipo de alimentación principal?')
    print('1. Omnívora')
    print('2. Vegetariana')
    print('3. Vegana')
    print('4. Basada en comida rapida')
    tipo_dieta = int(input(''))

    if validarTipoDieta(tipo_dieta) == False:
        print('Error. Opción invalida, digite un código entre el 1 y el 4.')
        tipo_dieta = int(input(''))

    return tipo_dieta, porciones_semanales



def validarDatoPorciones(dato):
    if dato > 3 or dato < 1:
        return False
    else:
        return True


def validarTipoDieta(dato):
    if dato > 4 or dato < 1:
        return False
    else:
        return True


def contarVegetarianos10plusYComidaRapida(tipo_dieta, porciones_semanales):
    global grupo_personas_1, grupo_personas_2
    
    if porciones_semanales == 3 and tipo_dieta == 2:
        grupo_personas_1 += 1

  
    if tipo_dieta == 4:
        grupo_personas_2 += 1

    return grupo_personas_1, grupo_personas_2

    



def main():
    global total_personas, opc
    
    while opc.lower() == 's':
        print('------------------------------------------------------------------------')
        total_personas += 1
        Tipo_dieta, porciones_semanales = ingresarDatos()
        grupo_personas_1, grupo_personas_2 = contarVegetarianos10plusYComidaRapida(tipo_dieta, porciones_semanales)

        opc = str(input('¿Desea continuar? (S/N)\n'))
        if opc.lower() != 's' and opc.lower() !='n':
            opc = str(input('Incorrecto. Digita s o n'))

    

    print(f'La cantidad de personas que consumen más de 10 porciones de fruta y verduras semanalmente y que tienen una dieta vegetariana son:{grupo_personas_1}')
    print(f'El porcentaje de personas que llevan una dieta basada en comida rapida son:{(grupo_personas_2 / total_personas) * 100}%')
        
main()
