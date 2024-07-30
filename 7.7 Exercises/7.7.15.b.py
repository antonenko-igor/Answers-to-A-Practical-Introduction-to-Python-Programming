# written by Antonenko Igor(Orsk)
secret = input("Enter a encrypted message: - ")
key = input("Enter a key: - ")
 
alphabet = "abcdefghijklmnopqrstuvwxyz"
decrypted = []
for i in range(len(secret)):
	letter = secret[i]
	if letter in alphabet:
		dec_shift = ((alphabet.index(letter) + 25) - alphabet.index(key[i]))%25
		decrypted.append(alphabet[dec_shift])
	else:
		decrypted.append(letter)
print("The decrypted message: ", "".join(decrypted))	