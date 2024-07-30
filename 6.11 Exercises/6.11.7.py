string = input("Enter a word:  ")

if string == string[::-1]:
	print("The word is the palindrome.")
else:
	print("The word is not the palindrome.")  