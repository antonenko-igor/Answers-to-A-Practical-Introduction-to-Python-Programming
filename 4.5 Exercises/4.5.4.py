credits = eval(input("How many credits have you taken?: "))
if credits <= 23:
	print("You are a freshman .")
elif credits <= 53:
    print("You are a sophomore .")
elif credits <= 83:
    print("You are a juniors.")
elif credits >= 84:
    print("You are a seniours.")        	