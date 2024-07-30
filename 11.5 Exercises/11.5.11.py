s1 = input("Enter a word:  ")
s2 = input("Enter a encrypted word: ")

if len(s1) != len(s2):
	print("No!")
else:
	d = {}
	for i in range(len(s1)):
		d[s1[i]] = s2[i]
	print(d)

c = 0
for i in range(len(s1)):
	if d[s1[i]] == s2[i] and s1[i] != s2[i]:
		c += 1
if c == len(s1):
	print("Yes")
else:
	print("No!")  