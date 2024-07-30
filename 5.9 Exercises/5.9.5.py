num = eval(input("Enter a number - "))
count = 0
for i in range(1,(num + 1)):
	if num % i == 0:
		count = count + i
print("The sum of the divisors is ",count)		