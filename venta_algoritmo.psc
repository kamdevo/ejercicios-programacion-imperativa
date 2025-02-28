Algoritmo venta_multiple
	Definir venta,descuento,neto_pagar Como Real
	Escribir 'Ingrese el valor de la venta'
	Leer venta
	Escribir 'Ingrese la forma de pago:'
	Escribir '1. Efectivo'
	Escribir '2. CHeque'
	Escribir '3. Tarjeta d�bito'
	Definir forma_pago Como Entero
	Escribir '4. Tarjeta cr�dito'
	Escribir '5. Cr�dito'
	Leer forma_pago
	
	Segun forma_pago Hacer 
		1: descuento <- venta * 0.2;
		2: descuento <- venta * 0.15;
		3: descuento <- venta * 0.10;
		4: descuento <- venta <- 0.05;
		5. descuento <- venta <- 0;
	De Otro Modo
		Escribir 'Opción no valida';
	FinSegun
	
	neto_pagar <- venta - descuento;
	
	Escribir 'Valor de venta: ',venta;
	Escribir 'Descuento: ',descuento;
	Escribir 'Valor neto a pagar: ',neto_pagar; 
FinAlgoritmo

