my_string = [4, 3, 6, 1, 7]
print(my_string)

# Primero, ingresa a la lista el ultimo digito como primer digito (posicion 4 a posicion 0) 
# y el ultimo digito como primer numero (posicion 0 a posicion 4).

my_string.insert(0, my_string[(len(my_string)-1)])
my_string.insert(len(my_string)-1, my_string[1])

# queda asi con los datos ingresados: my_string = [ 7, 4, 3, 6, 1, 7, 4]


# Ahora, se eliminan los digitos originales (es decir la posicion 1 y la posicion ultimo - 1) para que solo queden los digitos 
# que se ingresaron en la lista.
my_string.pop(1)
my_string.pop(len(my_string)-1) # elimina ahora si el ultimo digito y no un numero fuera del indice de la lista.

print(my_string)