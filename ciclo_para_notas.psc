Funcion nota_definitiva<- calcular_definitiva ( nota_parcial, nota_laboratorio, nota_quiz)
	Definir nota_definitiva Como Real;
	nota_definitiva <- (nota_parcial * 0.40)+(nota_laboratorio*0.35)+(nota_quiz*0.25);
FinSubProceso

Funcion ingresar_Datos(nota_parcial Por Referencia, nota_laboratorio Por Referencia, nota_quiz Por Referencia)
	Escribir "Nota del Parcial: ";
	Leer nota_parcial;
	
	Escribir "Nota del Laboratorio: ";
	Leer nota_laboratorio;
	
	Escribir "Nota del Quiz: ";
	Leer nota_quiz;
FinFuncion

Funcion estado <- determinar_estado(nota_definitiva)
	Definir estado Como Caracter;
	Si nota_definitiva < 3.0 Entonces
		estado <- "Perdió";
	Sino
		estado <- "Ganó";
	FinSi
FinFuncion

Funcion imprimir_resultados(nota_definitiva, estado, i)
	Escribir "Nota definitiva del estudiante ", i, ": ", nota_definitiva;
	Escribir "Estado: ", estado;
	Escribir "-----------------------------------";
FinFuncion

Proceso ciclo_para
	Definir nota_parcial, nota_laboratorio, nota_quiz, nota_definitiva Como Real;
	Definir estado Como Cadena;
	Definir i Como Entero;
	nota_parcial <-0;
	nota_quiz <- 0;
	nota_laboratorio <- 0;
	Para i <- 1 Hasta 3 Con Paso 1 Hacer
		Escribir "Ingrese las notas del estudiante ", i, ":";
		ingresar_Datos(nota_parcial, nota_laboratorio, nota_quiz);
		nota_definitiva <- calcular_definitiva(nota_parcial, nota_laboratorio, nota_quiz);
		estado <- determinar_estado(nota_definitiva);
		imprimir_resultados(nota_definitiva, estado, i);
	FinPara
FinProceso
