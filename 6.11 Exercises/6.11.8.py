amount = eval(input("How many email addresses?:  "))

nSt = 0
nPr = 0

for i in range(amount):
	y = input("Enter a email: - ")
	if y[-20:] == "@student.college.edu":
		nSt = nSt + 1
	if y[-17:] == "@prof.college.edu":
		nPr = nPr + 1
print("The number of student email addresses -  ",nSt, 
	  "The number of professor email addresses - ",nPr ) 