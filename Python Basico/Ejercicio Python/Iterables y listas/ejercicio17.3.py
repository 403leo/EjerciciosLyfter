my_list = [9, 4, 7, 1, 5]
smallest_number = my_list[0]

for number_counter in range (len(my_list)):
	if my_list[number_counter] < smallest_number:
		smallest_number = my_list[number_counter]

print(f"El menor valor es: {smallest_number}")


