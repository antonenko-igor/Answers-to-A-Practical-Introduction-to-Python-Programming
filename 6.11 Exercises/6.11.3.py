formula = input("Enter a formula:   ")
x = 0
y = 0
for i in formula:
	if i == "(":
		x = x + 1
	if i == ")":
		y = y + 1
if x == y:
	print("The formula is right.")
else:
	print("The formula is wrong.")  