d = {"Liam":1,"James":2,"Henry":3,"Daniel":4,"Levi":5,\
    "Jack":6,"John":7,"Leo":8,"Anthony":9,"Charles":10}
n = input("Enter a username:")
if n not in  d:
	print("The person is not a valid user of the system.")
p = eval(input("Enter a password: "))
if p == d[n]:
	print("You are logged.")
else:
	print("The password is invalid") 