Proceso sin_titulo
	Definir codigo, cantidad, precio_unitario, total_producto, total_venta Como Entero;
	codigo <- -1;
	Escribir "Antes del mientras";
	Mientras codigo <> 0 Hacer  //verdadera
		Escribir "Código [con 0 termina] :";
		Leer codigo;
		Si codigo <> 0 Entonces
			Escribir "Cantidad :";
			Leer cantidad;
			Escribir "Precio Unitario :";
			Leer precio_unitario;
			total_producto <- cantidad * precio_unitario;
			Escribir "Total producto :", total_producto;
            total_venta <- total_venta + total_producto;	
		FinSi		
	FinMientras
    Escribir 'El total de la venta es: ',total_venta;	
	Escribir "Después del mientras";
FinProceso