from random import shuffle

string = input("Enter a sentence:  ")
L = string.split()
shuffle(L)
print(" ".join(L)) 