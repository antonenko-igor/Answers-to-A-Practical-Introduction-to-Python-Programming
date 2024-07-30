temp = eval(input("Enter a temperature: "))
unit = eval(input("Unit: Celsius-1 или Fahrenheit-2 :"))
if unit == 1:
	print("The temperature is ",(9/5)*temp+32,"Fahrenheit.")
else:
    print("The temperature is",(5/9)*(temp-32),"Celsius.")	