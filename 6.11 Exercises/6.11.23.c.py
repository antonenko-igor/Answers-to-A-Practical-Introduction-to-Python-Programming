string = input("Enter a string to encrypt:  ")
block = eval(input("The integer that determines a breaks up of parts: "))
encrypted = ""
for i in range(block):
    for j in range(i,len(string),block):
        encrypted +=  string[j]
print(encrypted) 