L = eval(input("Enter a list of integers: "))

del L[0]
del L[-1:]
L.sort()
print(L) 	