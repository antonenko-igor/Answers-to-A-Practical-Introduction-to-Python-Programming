temp = eval(input("Enter a temperature in Celsius: "))
if temp < -273.15:
	print("The temperature is invalid!")
elif temp == -273.15:
    print("The temperature is absolute 0.")
elif temp < 0:
    print("The temperature is below freezing.")
elif temp == 0:
    print("The temperature is at the freezing point.")
elif temp < 100:
    print("The temperature is in the normal range.") 
elif temp == 100:
    print("The temperature is at the boiling point.")
elif temp > 100:
    print("The temperature is above the boiling point.")           	