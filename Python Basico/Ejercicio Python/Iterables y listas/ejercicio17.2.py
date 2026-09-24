my_list = [3, 6, 0, -2, 4]
is_there_negative_numbers = False

for number_counter in range (len(my_list)):
	if my_list[number_counter] <= 0:
		is_there_negative_numbers = True

if is_there_negative_numbers == True:	
	print("Hay al menos un número negativo o cero")
else: 
	print("No hay números negativos o ceros")
