string = input("Enter a word:  ")
x = " "

for i in string:
	if i in 'aeiou':
	    x = x + i 
print("The word contains the following vowels -",x)  