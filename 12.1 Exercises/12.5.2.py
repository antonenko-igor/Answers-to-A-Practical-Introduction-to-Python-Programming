lines = [line.strip() for line in open("grades.txt")]

count = 0
for line in lines:
	L = line.split(" ")
	if len(L) == 4:
		count += 1
print("The number of students are ",count) 