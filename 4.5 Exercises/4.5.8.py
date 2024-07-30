year = eval(input("Enter a year: "))
if  year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
	print("The leap year.")
else:
	print("Not the leap year.") 