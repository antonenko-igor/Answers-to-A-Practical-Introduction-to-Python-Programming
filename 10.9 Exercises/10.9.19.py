L = [[],[],[],[],[],[],[],[],[],[],[],[]]
print("To complete, enter - done")
while True:
	b = input("Enter a birthday in the format (month/day): ")
	if b == "done":
		break
	i = b.split("/")
	j = int(i[0]) - 1
	L[j].append(int(i[1]))

m = eval(input("Enter month to count the birthdays:"))
print("The amount of the birthdays is  ",len(L[m-1]))
print("The amount of the birthdays of March 25 is ",L[2].count(25)) 