Algoritmo Ejercicio_8_2
	Escribir 'Ingrese el numero de lapices a comprar: '
	Leer lapiz
	Si lapiz>=1000 Entonces
		prec2 <- lapiz*(85/100)
		Escribir 'precio por pagar de ', lapiz, ' lapices ', 'son ', prec2, ' pesos'
	SiNo
		prec1 <- lapiz*(90/100)
		Escribir 'precio por pagar de ', lapiz, ' lapices ', 'son ', prec1, ' pesos'
	FinSi
FinAlgoritmo
