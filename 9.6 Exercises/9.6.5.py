print("To complete, enter a negative number.")
score = 0
scores = []
grades = []

while score >= 0:
	score = eval(input("Enter a number of test scores:  "))
	scores.append(score)
for score in scores:
	if score > 90:
		grades.append("A")
	elif score > 60:
		grades.append("B")
	elif score > 60:
		grades.append("C")
	elif score > 50:
		grades.append("D")
	elif score > 40:
		grades.append("E")
	elif score > 0:
		grades.append("F")
	elif score < 0:
		scores.pop()
print(scores)
print(grades)
print("The number of A's is ",grades.count("A"))
print("The average of test scores -",sum(scores)/len(scores)) 