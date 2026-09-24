my_list = []
amount_of_numbers_in_list = int(input("Ingrese la cantidad de numeros en la lista: "))
amount_of_repeated_number = 0
number_to_append = 0

for number_counter1 in range (amount_of_numbers_in_list):
	number_to_append = int(input("Ingrese un numero a la lista: "))
	my_list.append(number_to_append)

number_to_search = int(input("Ingrese un numero a buscar en la lista: "))
for number_counter2 in range (amount_of_numbers_in_list):
	if my_list[number_counter2] == number_to_search:
		amount_of_repeated_number += 1

print(f" El numero {number_to_search} aparece {amount_of_repeated_number} veces.")
	


