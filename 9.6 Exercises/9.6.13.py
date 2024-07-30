from random import randint
win = 0
lost = 0
tie = 0
i = 1
print("Paper - 1,Rock - 2,Scissors - 3")
while True:
	r = randint(1,3)
	print("Round -",i)
	g = eval(input("Your turn- "))
	if r == 1 and g == 1 or r == 2 and g == 2 or r ==3 and g == 3:
		tie = tie + 1
	if r == 2 and g == 3 or r == 3 and g == 1 or r == 3 and g == 1 \
	   or r == 1 and g == 2:
		lost = lost + 1
	if r == 3 and g == 2 or r == 1 and g == 3 or r == 1 and g == 3 \
	   or r == 2 and g == 1:
		win = win + 1
	if lost == 3:
		print("The computer wins.")
		break
	if win == 3:
		print("The player wins.")
		break
	i = i + 1
	if i == 6:
		break
print("Game over.")
print("Ties - ",tie)
print("Loss - ",lost)
print("Wins - ",win) 