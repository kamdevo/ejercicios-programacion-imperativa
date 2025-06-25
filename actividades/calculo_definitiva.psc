Proceso sin_titulo
	Definir notas Como Real;
	Definir i, j, FIL, COL Como Entero;
	Dimension notas[3,4]; //de tama�o 3 filas y 4 columnas
	FIL <- 3; COL <- 4;
	notas[0,0] <- 3.5; notas[0,1] <- 4.8; notas[0,2] <- 3.7; notas[0,3] <- 0.0;
	notas[1,0] <- 3.8; notas[1,1] <- 2.8; notas[1,2] <- 4.1; notas[1,3] <- 0.0;
	notas[2,0] <- 4.8; notas[2,1] <- 3.4; notas[2,2] <- 3.9; notas[2,3] <- 0.0;
	escribir "      P1 | P2 | LA  | DE |";
	para i <- 0 hasta FIL-1 Hacer
		Escribir Sin Saltar (i+1), " -> ";
		para j <- 0 hasta COL-1 Hacer
			Escribir Sin Saltar  notas[i,j], " | ";
		FinPara
		Escribir "";
	FinPara
	
	// Recorrer la matriz para calcular la nota definitiva
	
FinProceso