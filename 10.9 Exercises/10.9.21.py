f = input("Enter a fraction:  ")
x = f.split("/")
a = int(x[0])
b = int(x[1])
while a != 0 and b != 0:
	if a > b:
		a = a % b
	else:
		b = b % a
c = a + b
a = int(x[0])/c
b = int(x[1])/c
print("The fraction in the lowest terms is  ",int(a),"/",int(b)) 