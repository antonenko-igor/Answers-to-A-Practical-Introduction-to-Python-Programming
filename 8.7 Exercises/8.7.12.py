# Igor Antonenko
s = input("Enter a phone number.")

if s[:2] =="1-" and len(s) == 14:
	s = s[2:]
else:
	s = s
w = "Wrong!"	
if s[3] == "-" and s[7] == "-":
	s = s.split("-")
	if len(s[0]) == 3 and len(s[1]) == 3 and len(s[2]) == 4:
		if "".join(s).isdigit():
			print("Right.")
		else:
			print(w)
	else:
		print(w)		
else:
	print(w) 