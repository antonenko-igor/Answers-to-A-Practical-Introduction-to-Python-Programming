width = eval(input("Enter a width: "))
height = eval(input("Enter a height: "))
count = 0
for i in range(height):
    for j in range(width):
        print(count % 10, end="  ")
        count = count + 1
    print(end="\n") 