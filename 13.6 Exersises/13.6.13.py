def change_case(s):
	string = ""
	for i in s:
		if i in "ABCDEFGHIJKLMOPQRSTUVWXYZ":
			string += i.lower()
		elif i in "abcdefghijklmnopqrstuvwxyz":
			string += i.upper()
	return string
print(change_case("PyThOn")) 