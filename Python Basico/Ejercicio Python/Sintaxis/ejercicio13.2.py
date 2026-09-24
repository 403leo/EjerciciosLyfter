numbers_sum = 0
number_equal_thirty = 0

for number in range (3):
	user_number = int(input(f"Enter number {number + 1} : "))
	if user_number == 30:
		number_equal_thirty = user_number
	numbers_sum += user_number

if numbers_sum == 30 or number_equal_thirty == 30:
	print("Correcto")
else: 
	print("Incorrecto")
	