c = eval(input('Enter an amount of change less than $1.00: '))
print(c // 25, " - quarters")
c = c % 25
print(c // 10, " - dimes")
c = c % 10
print(c // 5, " -  nickels")
c = c % 5
print(c // 1, " -  pennies")  