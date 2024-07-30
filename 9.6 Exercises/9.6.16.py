from random import choice,shuffle
characters = [" 5 "," # "," A "," ! "," 0 "," b "," $ "," z ",
             " x "," - "," + "," c "," & "]*2
shuffle(characters)
list_characters = []
for i in range(5):
    M = []
    for j in range(5):
        x = choice(characters)
        M.append(x)
        characters.remove(x)
    list_characters.append(M)
print(list_characters)
list_asteriks = [[" * " for _ in range(5)] for _ in range(5)]
for row in list_asteriks:
    print("   ".join(row))
count = 0
c = 0
print("To complete, press - 10")
print()
while True :   
    row_1 = int(input("Enter a coordinate of row- "))
    if row_1 == 10:
        break
    col_1 = int(input("Enter a coordinate of column - ")) 
    list_asteriks[row_1-1][col_1-1] = list_characters[row_1-1][col_1-1]   
    for row in list_asteriks:
        print("  ".join(row))
    row_2 = int(input("Enter a coordinate of row - "))
    col_2 = int(input("Enter a coordinate of column - "))
    list_asteriks[row_2-1][col_2-1] = list_characters[row_2-1][col_2-1]
    for row in list_asteriks:
        print("  ".join(row))
    if list_asteriks[row_1-1][col_1-1] == list_asteriks[row_2-1][col_2-1]:
        list_characters[row_1-1][col_1-1] = " * "
        list_characters[row_2-1][col_2-1] = " * "
        list_asteriks[row_1-1][col_1-1] = " * "
        list_asteriks[row_2-1][col_2-1] = " * "
        count = count + 1
        print("Right!")
        print()
    else:
        list_asteriks[row_1-1][col_1-1] = " * "
        list_asteriks[row_2-1][col_2-1] = " * "
        print("Wrong!")
        print()
    for row in list_characters:
        c = c + row.count(" * ")
    if c == 24:
        break
print("Game over.")
print("The number of correct guesses- ", count) 