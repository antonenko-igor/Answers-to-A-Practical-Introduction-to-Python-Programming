m = input("Enter a string to decrypt: ")

a = m[:(len(m)- (len(m)//2))]
b = m[-(len(m)//2):]

if a != b:
	b = b + " "

for i in range(len(a)):
	print(a[i] + b[i], end = "") 