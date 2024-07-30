string_1 = input("Enter the first string:  ")
string_2 = input("Enter the second string of the same length: ")
string = ""

if len(string_1) != len(string_2):
	print("Strings of different lengths")
else:
	for i in range(len(string_1)):
		string = string_1[i] + string_2[i]
		print(string,end = "") 