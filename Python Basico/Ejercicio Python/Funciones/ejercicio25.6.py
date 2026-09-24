# Separar funcionalidades en varias funciones

#  Una funcion para pasar la palabra a una lista

# Otra funcion para pasar la lista a a otra lista pero ordanada alfabeticamente

# Ottra funcion para devolver esta nueva lista de palabras ordenadas alfabeticamente a un string normal

# de ultimo, una funcion para llamar a las tres funciones y resolver el ejercicio 


#1. Funcion 

def string_word_to_list_of_words(chosed_word):	
    
    #Pasar palabra a lista
    lista_nueva = []
    
    # Atributo que va agregando un caracter de la palabra a recorrer y luego se borra
    # para continuar con la siguiente.
    # Por ejemplo:
    # Si encontre la palabra python que esta antes de un "-",
    # Va agregar primero la palabra "p", luego se borra y luego 
    # sigue con la palabra "y" y asi sucesivamente.
    new_word = ""
    
    # Se define un atributo de start_index para poder iniciar ya sea desde el
    # primer caracter de la palabra (que seria 0) o que empieze 1 indice mas desde 
    # el ultimo "-" que se encontro (por eso hace un start_index + 1)
    start_index = 0
    
    # Recorrer cada caracter de la palabra para encontrar un -
    for index in range(len(chosed_word)):
        if chosed_word[index] == "-":
        
            # Recorre los caracteres la palabra que esta antes de ese guion (-)  
            # o
            # despues de un guion (-) y antes de que se encuentre otro guion (-)
                for index1 in range(start_index, index):
                
                        # Una vez con el caracter, lo agrega al atributo
                        # de new_word hasta llegar al ultimo caracter y despues
                        # meter la palabra completa al primer indice de la nueva lista.
                        new_word += chosed_word[index1]
                
                # Agrega la nueva palabra a la lista. 	
                lista_nueva.append(new_word)
                
                # Vuelve a reiniciar el atributo de "new_word" para que quede vacio 
                # para la siguiente palabra
                new_word = ""
                
                # Actualizar el start_index para que empiece a agarrar 
                # la siguiete palabra que esta despues de un guion (-) 
                start_index = index + 1
    
    # La ultima palabra nunca lograra encontrarla porque no tiene 
    # un "-" entonces se debe buscar en un for por aparte
    
    
    # Recorre la palabra desde un indice mas del ultimo "-" encontrado
    # y hasta el final de la palabra.
    for index1 in range(start_index, len(chosed_word)):
    
        # Una vez con el caracter, lo agrega al atributo
        # de new_word hasta llegar al ultimo caracter y despues
        # meter la palabra completa al primer indice de la nueva lista.
        new_word += chosed_word[index1]
    
    # Agrega la nueva palabra a la lista. 	
    lista_nueva.append(new_word)

    
    return lista_nueva
    

#2. Metodos que ordenan la lista nueva

# Metodo que devuelve cual 

def is_order_list_of_two_wordsin_alphabetical_order(first_word, second_word):

    # Recibimos la palabra completa y comparamos solo el primer caracter de cada palabra para ver cual va primero

    # Recorremos el primer caracter de cada palabra recibida y comparamos cual es mayor y cual es menor 
    # para dar veridicto si la lista tiene las palabras ordenadas o no,
    
    # hacer atributo de position para poder definir hasta donde va a llegar a recorrer el caracter a una palabra.    
    position = 0
    
    # Mientras existan caracteres para comparar
    # un while porque no sabemo hasta cuantos caracteres va a comparar
    while position < len(first_word) and position < len(second_word):
    
        # Si el caract
        if first_word[position] < second_word[position]:
            return True  
        elif first_word[position] > second_word[position]:
            return False
        # Si son iguales, avanzamos al siguiente carácter
        position += 1               
            
    # Se devuelve el numero que tiene que ir primero en la lista.
    return True 


#Metodo que devuelve dos palabras ordenadas.
def order_list_of_two_words(first_word, second_word):

    # agrramos el meotod anterior de saber si esta ordenado o no
    # y si no,
    # lo unico que hacemos es ordenar las doa palabras si es false o true.
    if is_order_list_of_two_wordsin_alphabetical_order(
        first_word,
        second_word
    ):

        return first_word, second_word

    else:

        return second_word, first_word
            

    
def list_of_words_in_alphabetical_order(lista_nueva):

    # Ordenar la lista_nueva por orden alfabetico
    # Para esto, se hacen dos funciones, una para comparar solo dos palabras 
    # que hara que defina si una es mayor que otra y retornar si es verdadero o falso
    # y 
    # luego, otra funcion que igual compara dos palabras con el metodo anterior
    # y 
    # si alguno es mayor o menor, se ordena respectivamente.
    # Ej: [2,3,1] , compara los primeros dos elemtnos y pregunatara si asi como esta 
    # el 2 es mayor que 3 y como no, conmtinura comparando el 1 con el 3 y ordenara y 
    # asi sucesivamente.
    
    is_list_ordered = False

    while is_list_ordered == False:

        is_list_ordered = True
    
        #recorremos la lista nueva hasta el penultimo caracter para que no compare 
        # el ultimo con uno que no existe. Ej: Si recorro la palabra HOLA no puedo 
        # llegar a la ultima A porque si no buscaria un index+1 que no existe. 
        
        for index in range(len(lista_nueva)-1):
    
            #Primero, recorremos la lista e identificamos las primeras dos palabras
            # a comparar y las llamamos a una funcion que compara sus 
            # caracteres para ver cual se mete primero a la lista.
            # Antes, hacemos un if para que compruebe que no esta ubicado en el 
            # ultimo caracter porque si no podria comparar con el siguinet
            # y luego, modificamos la lista nueva, la palabra que va primero.
            
            #Si la lista no sigue ordenada, se sigue ordenando hasta que se devuelva 

        

            first_word = lista_nueva[index]
            second_word = lista_nueva[index + 1]

            # ¿Esta pareja está desordenada?

            if is_order_list_of_two_wordsin_alphabetical_order(
                first_word,
                second_word
            ) == False:

                # Como encontramos un desorden,
                # tendremos que hacer otra vuelta

                is_list_ordered = False

                # Ordenamos las dos palabras

                first_word, second_word = order_list_of_two_words(
                    first_word,
                    second_word
                )

                # Reemplazamos las palabras en la lista

                lista_nueva[index] = first_word
                lista_nueva[index + 1] = second_word

            
    return lista_nueva

        # quiero comprobar que si llego al ultimo numero no se me caiga 
        # la logica porque luego no encuentra un numero despues del ultimo numero
        
        
        
        # Primero, recorrreremos la lista con el indice y actual y el 
        # siguiente indice despues del actual para que se comparen
        # dos numeros
        
        
        
        
        
        # Llamar a un metodo que compara dos letras y defina cual 
        # va primero y cual va de segundo
        
        


# 3. Pasar la lista de palabras a un string con - entre cada palabra

def new_list_in_alphabetical_order_to_new_string(new_list):


    new_word = ""

    # Vamos a recorrer la lista y cada palabra se metera a la lista con un - a excepcion del ultimo
    for index in range (len(new_list)):

        # Llamamos al atributo de la nueva palabra y le agregamos el - si no es la ultima palabra
        if new_list[index] != new_list[len(new_list)-1]:
            new_word += new_list[index] + "-"
            continue
        else:
            new_word += new_list[index]

    return new_word


# Llamar a los tres metodos



def hyphenated_words(chosed_word):

    # Pasar de palabra a lista
    
    lista_nueva = string_word_to_list_of_words(chosed_word)
    
    print(chosed_word)
    print(lista_nueva)

    lista_ordenada = list_of_words_in_alphabetical_order(lista_nueva)

    print(lista_ordenada)

    new_word = new_list_in_alphabetical_order_to_new_string(lista_ordenada)

    print(new_word)

chosed_word = "python-variable-funcion-computadora-monitor"
hyphenated_words(chosed_word)