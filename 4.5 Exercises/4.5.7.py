num_1 = eval(input("Enter a number: "))
num_2 = eval(input("Enter a number: "))
dif = 0
if num_1 > num_2:
	dif = num_1 - num_2
else:
    dif = num_2 - num_1
if dif <= 0.001:
    print("Close")
else:
    print("Not close")    