sales = [
    {
        'date': '27/02/23',
        'customer_email': 'joe@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {
                'name': 'Iron',
                'upc': 'ITEM-324',
                'unit_price': 32.45,
            },
            {
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 12.54,
            },
        ],
    },
    {
        'date': '27/02/23',
        'customer_email': 'david@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 5.42,
            },
        ],
    },
    {
        'date': '26/02/23',
        'customer_email': 'amanda@gmail.com',
        'items': [
            {
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 3.42,
            },
            {
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 17.54,
            },
        ],
    },
]

upc_dictionary = {}

# Recorrer la lista de ventas
for index1, sale in enumerate(sales):

    # Recorrer cada producto de la venta
    for index2, item in enumerate(sale['items']):

        #print(f"Value {index1}.{index2}: {item}")

        if item['upc'] not in upc_dictionary:
            #print(f"Nuevo UPC: {item['upc']}")
            upc_dictionary[item['upc']] = item['unit_price']
        else:
            #print(f"Sumando al UPC: {item['upc']}")
            upc_dictionary[item['upc']] += item['unit_price']

print("Resultado:")

for key, value in upc_dictionary.items():
    print(f"UPC: {key} - Total Sales: {value}")