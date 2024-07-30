a = eval(input("Enter a test score - "))
b = eval(input("Enter a test score - "))
if a < b:
	high_1 = b
	high_2 = a 
else:
	high_1 = a 
	high_2 = b
for i in range(8):
	num = eval(input("Enter a test score -"))
	if  high_2 < num < high_1:
		high_2 = num	
	elif num > high_1:
		high_2 = high_1
		high_1 = num	
print("The second largest score -",high_2) 