def list_numbers_to_prime_numbers_list(lista):
	# Un atributo de la nueva lista con los numeros primos.
	prime_numbers_list = []
	for index in range(len(lista)):
		if number_is_prime(lista[index]) == True:
			prime_numbers_list.append(lista[index])
	return prime_numbers_list
	
	
# Hacer un metodo booleano para retonar si un 
# numero es primo o no (este devolveria un true o un false)

def number_is_prime (number):

	# Un atributo booleano para determinar si el numero es primo o no.
	is_prime = True

	if number < 2:
		is_prime = False
	else:
		# Se saca la raiz cuadrada del numero escogido y 
		# se toman en cuenta los numeros pirmos que van antes de ese resultado.
		
		square_root_number = number ** 0.5
		
		#Agarrar los numeros PRIMOS que van antes de la raiz cuadrada.
		# Empieza del segundo numero (que seria el 1 porque empieza en cero) porque 
		# el 1 siempre va a dar el residuo 0 con cualquier numero entonces no vale la pena
		# Se suma ademas el 1 para que el rango llegue hasta el numero de la raiz cuadrada 
		# sin decimales.
		# Se pasa a int el square_root_number_without_decimals porque aunque se le quito decimales
		# el resultado sigue siendo un float y el rango solo acepta enteros. 
		for index in range(2, int(square_root_number)  + 1):
		
			# Se calcula los residuos de los numeros PRIMOS que van antes de la raiz cuadrada
			# del numero anterior
			if number % index != 0:
				is_prime = True
				continue
			else:
				is_prime = False
				break
	return is_prime
		
numbers_list = [1, 4, 6, 7, 13, 9, 67]		
#Mostrar la lista original
print("Lista original:")
print(numbers_list)

print(1%2 != 0) 

# Aplicamos el metodo creado y mostramos la lista modificada
print(list_numbers_to_prime_numbers_list(numbers_list))