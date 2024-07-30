height = eval(input("How high is a diamond?:  "))
h = int(height/2)
for i in range(h):
	print(" "*((h-1)-i),"*" " "*i + "*")
for i in range(h):
	print(" "*i,"*" " "*((h-1)-i) + "*")
input() 