def sum_numbers():
	list_of_numbers = [4, 6, 2, 29]
	total_sum_of_list_of_numbers = 0
	for index in range(len(list_of_numbers)):
		total_sum_of_list_of_numbers += list_of_numbers[index]
	return total_sum_of_list_of_numbers
	
print(f"La suma de total de numeros es de {sum_numbers()}")

