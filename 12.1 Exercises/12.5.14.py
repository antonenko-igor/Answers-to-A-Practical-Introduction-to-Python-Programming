words = [line.strip() for line in open('wordlist.txt')]
s = input("Enter a string ")
s_l = s.lower()
L = s_l.split()
for i in L:
 	if i not in words:
 		print("The word ",i," is misspelled") 