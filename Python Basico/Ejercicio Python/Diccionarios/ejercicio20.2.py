employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

# Se agregan diccionario a esta lista
new_company = {}
# Recorrer la lista de diccionarios de employee para poder encontrar sus departamentos asignados, 
# y luego clasificarlos por departamento.

# se agrega un indice para recorrer
for key in employees:   
        #departamento = employees["department"]
    # Si el departamento no esta en el nuevo diccionario.
    
    if key['department'] not in new_company:
                print(f"Nuevo Departamento: {key['department']}")
                new_company[key['department']] = [
                    {
                        "name": key['name'],
                        "email": key['email']
                    }
                ]

    else:
            # Si ya esta, busca el empleaado del deparamento y lo agrega a la lista de empleados
        print(f"Agregando empleado al Departamento ya creado: {key['department']}")
        # Se agrega un nuevo dato a la lista del diccionario del departamento escogido.    
        new_company[key['department']].append({
            "name": key['name'],
            "email": key['email']
        }
        )


print("Resultado: ")
for key, value in new_company.items():    
    print(key, ":", value)
