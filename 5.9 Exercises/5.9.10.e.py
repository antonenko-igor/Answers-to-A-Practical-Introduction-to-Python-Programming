a = eval(input('Enter a test score: '))
b = eval(input('Enter a test score: '))
if a < b:
    low_1 = a
    low_2 = b
else:
    low_1 = b
    low_2 = a
s = a + b
for i in range(8):
	a = eval(input("Enter a test score: "))
	s = s + a
	if low_1 < a < low_2:
		low_2 = a
	elif a < low_1:
		low_2 = low_1
		low_1 = a
print("The average without the two lowest scores - ",(s-low_1-low_2)/8,) 