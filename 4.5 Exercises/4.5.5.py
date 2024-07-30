from random import randint

rand = randint(1,10)
num = eval(input("Enter a number: "))
if num == rand:
	print("You are right!")
else:
    print("Wrong! The number is ",rand)	