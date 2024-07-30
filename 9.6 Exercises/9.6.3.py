weight = eval(input("Enter a weight (in kg):  "))

while weight < 0:
	weight = eval(input("Error! Enter a correct weight:  "))
print("The weight is ",weight*2.2, "pounds") 