# Agarrar un contador , agarrar el tamano de la palabra y quitarle en base a lo que tiene el contador 
# actualente y asi hasta que el contador ya sea mayor 


def flip_word():
	chosed_word = "Hola mundo"
	flipped_word = ""
	for index in range(len(chosed_word)):
		flipped_word = flipped_word + chosed_word[(len(chosed_word)-1)-index]
	return flipped_word
	
print(flip_word())