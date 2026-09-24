def convertir_a_entero(lista):
    
    for index in range(len(lista)):
        try:
            lista[index] = int(listaNueva[index])
        except ValueError:
            raise ValueError("La edad debe ser un número.")
    print(f"{lista[index]} convertido a {listaNueva[index]} No se pudo convertir el elemento{lista[index]}")

