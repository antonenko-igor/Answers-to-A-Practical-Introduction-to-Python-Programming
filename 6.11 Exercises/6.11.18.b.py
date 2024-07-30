string = input("Enter a string:   ")
letter = input("Enter a letter:   ")

x = 0
for i in range(len(string)):	
	if string[i] == letter:
		x = x + 1
print("The letter ",letter,"occurs in the string ",x,"time(s).") 