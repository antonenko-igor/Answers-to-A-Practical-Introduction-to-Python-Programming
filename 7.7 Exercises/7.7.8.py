num = eval(input("Enter an integer:  "))

N = []
for i in range(1,num + 1):
	if num % i == 0:
		N.append(i)
print("The factors of the integer ", N)		