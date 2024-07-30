print("To complete, enter - done.")
d = {}
while True:
	n = input("Enter a product name: ")
	if n == "done":
		break
	p = eval(input("Enter a price: "))
	d[n] = p 
x = eval(input("Enter a dollar amount: "))
for i in d:
	if d[i] < x:
		print(i)  