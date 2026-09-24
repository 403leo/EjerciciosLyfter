original_list = []
bigger_number = 0

for number_counter in range (10):
	user_number = int(input("Enter number " + str(number_counter + 1) + ": "))
	original_list.append(user_number)
	if original_list[number_counter] > bigger_number:
		bigger_number = original_list[number_counter]
	
print(f"{original_list} . El numero mas alto fue {bigger_number}")
