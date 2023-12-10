Algoritmo Ejercicio_7_2
	// Diagrama de flujo para obtener la suma de diez cantidades mediante la utilización de un ciclo "Mientras"
	Escribir 'Ingresa un numero: '
	Leer num
	i <- 1
	acc <- 0
	Mientras  i<=num Hacer
		Escribir i , " "Sin Saltar
		acc <- acc+i
		i <- i+1
	FinMientras
	Escribir ''
	Escribir 'Suma: ', acc
FinAlgoritmo
