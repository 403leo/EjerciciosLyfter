def number_of_uppercases_and_lowercases_words():
	chosed_word = "I love Nacion Sushi"
	amount_of_uppercases_words = 0
	amount_of_lowercases_words = 0
	for index in range(len(chosed_word)):
		if 'A' <= chosed_word[index] <= 'Z':
			amount_of_uppercases_words += 1
		if 'a' <= chosed_word[index] <= 'z':
			amount_of_lowercases_words += 1
	print(f"There’s {amount_of_uppercases_words} upper cases and {amount_of_lowercases_words} lower cases")
	
number_of_uppercases_and_lowercases_words()