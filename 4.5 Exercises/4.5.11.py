hour = eval(input("Enter hour:  "))
unit = eval(input("am (1) or pm (2)? "))
future = eval(input("How many hours ahead?  "))
if  unit == 1 and future <= 3:
	print("New hour: ",(hour + future)%12, "am")
if  unit == 1 and future > 3:
	print("New hour: ",(hour + future)%12, "pm")
if  unit == 2 and future <= 3:
	print("New hour: ",(hour + future)%12,  "pm")
if  unit == 2 and future > 3:
	print("New hour: ",(hour + future)%12,  "am")  