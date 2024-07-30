string = input("Enter a string to decrypt: ")
decrypted = ""
for i in range(3):
    for j in range(i,14,5):
        decrypted += string[j]
print(decrypted) 