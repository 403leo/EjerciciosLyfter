list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]
first_name_and_first_surname_diccionary = {}

#Meter cada elemento en el diccionario agarrando 
# el primer indice de cada lista (key y value respectivmente) con un loop

for counter_number1 in range (len(list_a)):
		first_name_and_first_surname_diccionary[list_a[counter_number1]] = list_b[counter_number1]
	
print(first_name_and_first_surname_diccionary)