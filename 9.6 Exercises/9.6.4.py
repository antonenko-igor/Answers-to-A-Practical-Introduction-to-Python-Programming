c = 0
p = 0
while p != 12345 and c <= 4:
	p = eval(input("Enter a password(xxxxx):"))
	c = c + 1	
	if p == 12345:
		print("You are logged in to the system.")
	else:
		print("Invalid password.Enter a correct password:  ")
		print("You have ",5-c,"attemps left.")	
if p != 12345 and c == 5:
	print("You are kicked off of the system!") 