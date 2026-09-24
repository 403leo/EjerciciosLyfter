my_list = [10, 20, 30, 40, 50]
repetad_numbers_list = []
average_number = 0
sum_of_numbers = 0

for number_counter1 in range (len(my_list)):
	sum_of_numbers += my_list[number_counter1]
	
average_number = sum_of_numbers / len(my_list)
		
for number_counter2 in range (len(my_list)):
	if my_list[number_counter2] > average_number:
		repetad_numbers_list.append(my_list[number_counter2])
	
print(f"Promedio: {average_number}")
print(f"Nueva lista: {repetad_numbers_list}")


