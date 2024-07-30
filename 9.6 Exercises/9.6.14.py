from random import randint
money = 100
while True:
	p = randint(0,1)
	guess = eval(input("Heads(1) or Tails(0) - "))
	if p == guess:
		money = money + 9
		print("Right!")
	else:
		money = money - 10
		print("Wrong!")
	print("The amount of money",money)
	if money >= 200:
		print("You have won! Your money - ",money)
		break
	if money <= 0:
		print("You have lost.Your money - ",money)
		break 