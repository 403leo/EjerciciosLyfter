list_of_keys = ["access_level", "age"]
employee = {
	"name": "John",
	"email": "john@ecorp.com",
	"access_level": 5,
	"age": 28
}

# Recorrer la lista que contiene las keys que se desean eliminar
# En cada iteración, la variable 'key' almacena directamente uno de los
# elementos de la lista ("access_level" y luego "age").
for key in list_of_keys:

    employee.pop(key)

print(employee)

