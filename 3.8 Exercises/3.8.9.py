hour = eval(input("Enter an hour between 1 and 12: "))
x = eval(input("How many hours ahead?: "))
print("New hour: ",(hour + x)%12) 