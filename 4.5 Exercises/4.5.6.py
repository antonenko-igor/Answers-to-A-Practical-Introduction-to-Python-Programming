items = eval(input("How many items are you buying?:  "))
if items < 10:
	print("The total cost is: ",items*12)
elif items <= 99:
	print("The total cost is: ",items*10)
elif items >= 100:
    print("The total cost is: ",items*7)	