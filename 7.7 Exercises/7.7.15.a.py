# written by Antonenko Igor(Орск)
# one-time pad (The Vigenère cipher)

from random import randint
message = input("Enter a message: - ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
secret = []
key = []
num = []
for i in range(len(message)):
	char = message[i].lower()
	if char in alphabet:
		shift = randint(0,25)
		num.append(shift)
		key.append(alphabet[shift])
		enc = (alphabet.index(char) + shift)%25
		secret.append(alphabet[enc])
	else:
		secret.append(char)
print("The encrypted message: ", "".join(secret))
print("The key: ","".join(key)) 