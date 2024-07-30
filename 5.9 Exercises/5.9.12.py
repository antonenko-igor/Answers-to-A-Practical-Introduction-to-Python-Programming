from random import randint
s = 0

for i in range(5):
	num = randint(1,10)
	guess = eval(input("Enter a guess -"))
	if guess == num:
		s = s + 10
	else:
		s = s - 1
print("Your score -",s)		