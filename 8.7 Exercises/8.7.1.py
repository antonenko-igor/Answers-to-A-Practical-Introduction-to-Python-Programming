s = input("Enter some text:  ")
s = s.lower()
c = 0
l = s.split()
for i in l:
	if i == "the" or i == "a" or i == "an":
		c = c + 1
print("The number of articles is ",c)	