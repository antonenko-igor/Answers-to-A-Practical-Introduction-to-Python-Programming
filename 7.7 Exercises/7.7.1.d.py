L = eval(input("Enter a list of integers: "))
flag = 0

for i in L:
	if i == 5:
		flag = 1		
if flag == 1:
	print("Yes")
else:
	print("No")  