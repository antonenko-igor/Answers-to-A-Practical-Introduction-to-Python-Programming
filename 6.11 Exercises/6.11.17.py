s = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(s)):
	print(s[i: : ] + s[ :i: ],end = " ")
	print() 