numerator = int(input("Enter the numerator of a fraction: "))
denominator = int(input("Enter the denominator of a fraction: "))
digit_position = int(input("Enter the position of the desired digit: "))

decimal = numerator / denominator

digit = int(decimal * 10**digit_position) % 10
print("The digit with a position ", digit_position, "is:", digit) 