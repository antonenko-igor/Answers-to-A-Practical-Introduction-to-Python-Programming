score = eval(input("Enter a test score:  "))
highest = score
lowest = score

for i in range(9):
	score = eval(input("Enter a test score:  "))
	if score > highest:
		highest = score
	if score < lowest:
		lowest = score
print("The highest score - ",highest )
print("The lowest - ",lowest)		