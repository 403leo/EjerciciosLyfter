user_words_list = []
words_with_more_than_four_letterrs = []

for word_counter in range (5):
	user_word = input("Ingrese una palabra: ")
	user_words_list.append(user_word)
	# Saber cantidad de letras de la palabra actual
	if(len(user_words_list[word_counter])) > 4:
		words_with_more_than_four_letterrs.append(user_words_list[word_counter])
		
print(user_words_list)
print(words_with_more_than_four_letterrs)


