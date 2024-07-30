words = [line.strip() for line in open('wordlist.txt')]
ten = 0
seven = 0
for word in words:
	if len(word) == 10:
		ten += 1
	if len(word) == 7:
		seven += 1
if ten > seven:
	print("There are more ten-letter words - ", ten, ">", seven)
else:
	print("There are more seven-letter words - ", ten, "<", seven)  