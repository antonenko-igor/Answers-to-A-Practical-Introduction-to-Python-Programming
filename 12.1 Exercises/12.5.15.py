w = input("Enter a word(with *):   ")

words = [line.strip() for line in open('wordlist.txt')]

for word in words:
	s = ""
	if len(w) == len(word):		
		for i in range(len(w)):
			if w[i] == word[i] or w[i] == "*":
				s += word[i]
			else:
				break
		if len(s) == len(w):
			print(s) 