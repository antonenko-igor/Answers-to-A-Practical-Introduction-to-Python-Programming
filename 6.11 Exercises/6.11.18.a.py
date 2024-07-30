string = input("Enter a string:   ")

for i in range(len(string)):
	letter = input("Enter a letter:  ")
	if string[i] == letter:
		print("The letter is in the word.")
	else:
		print("The letter is not in the word.") 		