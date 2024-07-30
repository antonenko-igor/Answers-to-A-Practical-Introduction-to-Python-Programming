feet = eval(input("Enter a length in feet:  "))
print("""
1 convert into inches,
2 convert into yards,
3 convert into millimeters,
4 convert into centimeters,
5 convert into meters,
6 convert into miles,
7 convert into kilometers""")

x = eval(input(" >  "))
feet = feet * 1
inches = feet * 12
yards = feet *0.33333
millimeters = feet * 304.8
centimeters = feet * 30.48
meters = feet * 0.3048
miles = feet * 0.0001893939
kilometers = feet *0.0003048

convert = [feet, inches, yards, millimeters, centimeters, meters, miles, kilometers]
print(convert[x]) 