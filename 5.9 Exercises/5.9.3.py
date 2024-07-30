from math import log

count = 0
n = eval(input("Enter a value n: "))
for i in range(2,(n+1)):
	    count = count + (1/i)        
print("For", n,"  ",(1 + count) - log(n))	