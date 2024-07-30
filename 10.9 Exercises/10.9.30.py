"""
IDLE Shell 3.11.4- the output incorrect.
Use py.exe
"""
n = eval(input("Enter a height of Pascal’s triangle: "))
L = []
 
for i in range(0, n):
    r = ["1"] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            r[j] = str(int(L[i-1][j-1]) + int(L[i-1][j])) 
    L.append(r) 
for i in range(len(L)):
	s = " ".join(L[i])
	print("{:^100s}".format(s))
input() 