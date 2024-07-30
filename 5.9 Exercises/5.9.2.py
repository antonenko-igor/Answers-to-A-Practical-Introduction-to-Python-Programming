count = 0
for i in range(1,101):
	if (i**2) % 10 == 4:
		print(i ,"  ", i**2)
		count = count + 1
print("The number of numbers ending in 4 is", count)

for i in range(1,101):
	if (i**2) % 10 == 9:
		print(i,"  ", i**2)
		count = count + 1
print("The number of numbers ending in 9 is",count) 