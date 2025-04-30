import math
def es_triangulo(lado_a, lado_b, lado_c):
    es_tringulo_valido = False
    if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
            es_tringulo_valido = True
    return es_tringulo_valido

def calcular_semiperimetro(lado_a, lado_b, lado_c):	
    semiperimetro = (lado_a + lado_b + lado_c) / 2
    return semiperimetro

def calcular_area(lado_a, lado_b, lado_c):
    semiperimetro = calcular_semiperimetro(lado_a, lado_b, lado_c)
    area = math.sqrt(semiperimetro * (semiperimetro - lado_a) * (semiperimetro - lado_b) * (semiperimetro - lado_c))
    return area

def imprimir_resultados(lado_a, lado_b, lado_c, area):
    print("Lados del triángulo: ", lado_a, ", ", lado_b, ", ", lado_c)
    print("Área calculada: ", area)

def main():
    print("Área del Triángulo:")
    lado_a = float(input("Ingrese Lado 1:"))
    lado_b = float(input("Ingrese Lado 2:"))
    lado_c = float(input("Ingrese Lado 3:"))
    print('Área del triangulo: ')	
    if es_triangulo(lado_a, lado_b, lado_c):
        area = calcular_area(lado_a, lado_b, lado_c)
        imprimir_resultados(lado_a, lado_b, lado_c, area)
    else:
        print("Los lados ingresados no forman un triángulo válido.")


lado_a = 5
lado_b = 4
lado_c = 4.5
#Programa Principal
main() #Invoca la función main
