L = []
print("To complete, enter - done")
while True:
	s = input("enter a football score in the format (winning score-losing score): ")
	if s == "done":
		break
	x = s.split("-")
	L.append(int(x[0]))
	L.append(int(x[1]))
print(L)
print("The highest score -",max(L))
print("The lowest score - ",min(L)) 