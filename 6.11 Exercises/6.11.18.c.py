string = input("Enter a string:   ")
letter = input("Enter a letter:    ")

index = " "
for i in range(len(string)):
	if string[i] == letter:
		index = index + str(i) 
if index == " ":
	print("The letter is not in the string.")
else:
	print("The index of the first occurrence of the letter - ", index[1]) 