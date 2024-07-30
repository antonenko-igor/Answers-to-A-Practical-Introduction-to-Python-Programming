L1 = eval(input("Enter a first list: "))
L2 = eval(input("Enter a second list: "))
flag = 0
for ent in L2:
	if ent in L1:
		flag = 1
if flag == 1:
	print("There are items in common. ")
else:
	print("There are not items in common.") 