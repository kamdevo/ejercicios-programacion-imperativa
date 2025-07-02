Proceso sin_titulo
	definir num, i, mayor, menor como real;
	definir lista_reales Como Real;
	dimension lista_reales[15];

	para i<-0 hasta 14 Hacer
		escribir "Digita el número #", i+1;
		leer num;
	FinPara
	menor <- lista_reales[0];
	mayor <- lista_reales[0];
	
	para i <-0 hasta 14 Hacer
		si lista_reales[i] < menor entonces 
			menor <- lista_reales[i];
		FinSi
		
		si lista_reales[i] > mayor Entonces
			mayor <- lista_reales[i];
		FinSi
	FinPara
	escribir "El número mayor es: ", mayor;
	Escribir "El número menor es: ", menor;
FinProceso
