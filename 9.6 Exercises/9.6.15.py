from random import choice
C = ["Canada","Russian","China","Germany","Spain","Japan",
     "Indonesia","Polen","Chile"]
c = choice(C)
k = list(c)
A = []
for j in range(len(c)):
	A.append("-")
print(A)
count = 0
print("The first letter is uppercase.")
while "-" in A and count < 5:	
	letter = input("Enter a letter - ")
	if letter in k:
		for i in range(len(k)):
			if k[i]==letter:
				A[i]=letter
	else:
		count = count + 1
		print("The letter was not found.")
		print("Guesses left - ",5 - count)
	print(" ".join(A))
if count >= 5:
	print("You have lost!")
	print("The word is - ",c) 