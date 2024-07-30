word = input("Enter a word:    ")
words = [line.strip() for line in open('wordlist.txt')]
if word in words:
	print("Yes")
else:
	print("No")  