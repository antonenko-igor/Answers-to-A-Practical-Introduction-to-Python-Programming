def first_diff(string1,string2):
	if len(string1) < len(string2):
		l = len(string2)
	else:
		l = len(string1)
	for i in range(l):
		if string1 == string2:
			return -1
		elif string1[i] != string2[i]:
			return ("The first location in which the strings differ. ",i)
print(first_diff("python","pythun")) 
