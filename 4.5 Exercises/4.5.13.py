from random import randint

print("Rock - 1, Paper - 2, Scissors - 3")

win = 0
lost = 0
tie = 0

for i in range(5):
	host = randint(1, 3)
	print()
	user = eval(input("Make your move:  "))
	if host == user:
		tie = tie + 1
	if host == 1 and user == 3 or host == 2 and user == 1 or host == 3 \
	   and user == 2:
		lost = lost + 1
	if user == 1 and host == 3 or user == 2 and host == 1 or user == 3 \
	    and host == 2:
		win = win + 1
if tie == 5:
	print("Tie")
else:
	if win > lost:
		print("You won.")
	else:
		print("You lost.") 