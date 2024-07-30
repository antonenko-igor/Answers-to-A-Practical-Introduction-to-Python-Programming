flag = 0
for i in range(10):
	score = eval(input("Enter a test score:  "))
	if score > 100:
		flag = 1
print()
if flag == 1:
	print("The value over 100 has been entered.") 