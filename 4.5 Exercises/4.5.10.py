from random import randint

for i in range(1,11):
	num_1 = randint(1,10)
	num_2 = randint(1,10)
	print("Question",i,"  ", num_1,"X",num_2)
	mul = eval(input())
	if num_1*num_2 == mul:
		print("Right!")
	else:		
	    print("Wrong! The answer is"," ", num_1*num_2)	