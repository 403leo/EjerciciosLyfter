original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers_list = []
original_list_size = len(original_list)-1
number_counter = 0

while number_counter <= original_list_size:

    print("----------------")
    print("Indice:", number_counter)
    print("Lista actual:", original_list)
    print("Lista numeros impares:", odd_numbers_list)
        

    if original_list[number_counter] % 2 != 0:
        # Numero seleccionado con el indice
        odd_numbers_list.append(original_list[number_counter])
        original_list.pop(number_counter)
        original_list_size = len(original_list)-1

    # Si elimino un elemento, no incremento el contador, porque el siguiente elemento se mueve a la posición del elemento eliminado
    else:   
        number_counter += 1

# Numeros pares
print("------------------------------------------------------------------------------------------------")

print("Numeros pares:", original_list)
print(original_list)
#Numeros impares
print("----------------")
print("Numeros impares:", odd_numbers_list)
print(odd_numbers_list)
