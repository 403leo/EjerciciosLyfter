products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]


# Se agrega diccionario a esta lista de los productos con sus categorías
products_by_category = {}

# Recorrer la lista de diccionarios de products para poder encontrar sus categorías asignadas, 
# y luego clasificarlos por categoría y sumar sus precio agregandolo como un precio total.

# se hace un for recorriendo cada key de diccionario de la lista de productos
for key in products:   
    # Si el producto no esta en el nuevo diccionario.
    
    if key['category'] not in products_by_category:
                print(f"Nueva Categoria: {key['category']}")
				# Se agrega el nuevo key de diccionario con su key y value
                products_by_category[key['category']] = [
                    {
                        'total_price' : key['price']
                    }
                ]

    else:
            # Si ya esta, agrega un producto mas a la lista ya creada del
			# diccionario de esa categoria actual.
        print(f"Agregando producto a la categoria ya creada: {key['name']}")
        # Se agrega un nuevo producto a la lista del diccionario de la categoría escogida. 
		# Y ademas, se suma los precios de cada producto de la categoria
        products_by_category[key['category']] = [
            {
                'total_price' : products_by_category[key['category']][0]['total_price'] + key['price']
            }
        ]


print("Resultado: ")
for key, value in products_by_category.items():    
    print(key, ":", value)
