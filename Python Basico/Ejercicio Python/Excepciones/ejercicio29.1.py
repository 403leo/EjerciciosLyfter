#Crear calculadora

# Hacer una funcion por cada operacion

# 1. Suma

def suma_numero_actual_mas_numero_escogido(numero_actual, numero_a_sumar):
    numero_total = numero_a_sumar + numero_actual
    return numero_total
    
# 2. Resta

def resta_numero_actual_mas_numero_escogido(numero_actual, numero_a_sumar):
    numero_total = numero_actual - numero_a_sumar
    return numero_total
    
# 3. Multiplicacion

def multiplicacion_numero_actual_mas_numero_escogido(numero_actual, numero_a_sumar):
    numero_total = numero_a_sumar * numero_actual
    return numero_total
    
# 4. Division

def division_numero_actual_mas_numero_escogido(numero_actual, numero_a_sumar):
    numero_total = numero_actual / numero_a_sumar
    return numero_total
    

def menu_operaciones(numero_actual):

    

    
        opcion = 0
        # Hacer un while para que el usuario pueda escopger si se quiere salir o no del menu de operaciones

        while opcion != 6:

            # Hacer el try para agarrar excepcion de que no coloque letras en ves de numeros
            try:

                # Realizar con opciones 
                print ("1. Suma")
                print ("2. Resta")
                print ("3. Multiplicación")
                print ("4. División")
                print ("5. Borrar resultado")
                print ("6. Salir")
                print(f"Numero actual: {numero_actual}")
                opcion = int(input("Escoga una de las siguienets opciones: "))
                
                if opcion == 1:
                    numero_a_sumar = int(input("De un numero a sumar con el actual:"))
                    numero_actual = suma_numero_actual_mas_numero_escogido(numero_actual, numero_a_sumar)
                    
                elif opcion == 2:
                    numero_a_sumar = int(input("De un numero a sumar con el actual:"))
                    numero_actual = resta_numero_actual_mas_numero_escogido(numero_actual, numero_a_sumar)

                elif opcion == 3:
                    numero_a_sumar = int(input("De un numero a sumar con el actual:"))
                    numero_actual = multiplicacion_numero_actual_mas_numero_escogido(numero_actual, numero_a_sumar)

                elif opcion == 4:
                    try:
                        numero_a_sumar = int(input("De un numero a sumar con el actual:"))
                        numero_actual = division_numero_actual_mas_numero_escogido(numero_actual, numero_a_sumar)
                    except ZeroDivisionError:
                        print("Error [ZeroDivisionError]: No se puede dividir entre cero.")

                elif opcion == 5:
                    numero_actual = 0

                elif opcion == 6:
                    print("Saliendo del menu de operaciones")
                    break
                else:
                    print("Opcion invalida, por favor escoja una opcion valida")    

                print(f"Numero actual: {numero_actual}")
            except ValueError as e:
                    print(f"Error [ValueError]: Entrada inválida. Detalles: {e}")

# llamar a la funcion de menu_operaciones 

# Numero actual a actualizar
def main():
    numero_actual = 20
    menu_operaciones(numero_actual)


main()