print("To complete, enter - done.")
d = {}
while True:
	n = input("Enter a product name: ")
	if n == "done":
		break
	p = eval(input("Enter a price : "))
	d[n] = p 
while True:
	a = input("Enter a product name: ")
	if a in d:
		print(d[a])
	else:
		print("The product is not in the dictionary.")  