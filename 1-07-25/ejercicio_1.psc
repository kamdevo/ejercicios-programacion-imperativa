Proceso sin_titulo
	definir num, suma, i, numeros como entero;
	suma <- 0;
	dimension numeros[10];
	para i<-0 hasta 9 Hacer
		Escribir "Digita el numero",i+1,".";
		Leer num;
		numeros[i] <- num;
		suma <- suma + numeros[i];
	FinPara
	escribir suma;
FinProceso
