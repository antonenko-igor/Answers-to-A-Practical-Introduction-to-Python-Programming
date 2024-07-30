L = []
print("To complete press - done")
while True:
	h = input("enter a height in the format (feet,inches) :  ")
	if h == "done":
		break
	x = h.split("'")
	k = x[0]
	n = int(x[0]) + float("{:.2f}".format(int(x[1])*(1/12)))
	L.append(n)
for i in range(4,13):
	count = 0
	for j in L:
		if int(j) == i:
			count +=1
	print(i,"-footers = ",count) 