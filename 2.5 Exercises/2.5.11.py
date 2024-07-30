"""
Run the program using py.exe.
Output of IDLE Shell 3.11.4 is incorrect

"""
length = eval(input("How wide is a box?: "))
height = eval(input("How hight is a box?: "))
print("* "*length)
for i in range(1,(height-1)):
	print("*" , "  "*(length-2)+ "*" )
	
print( "* "*length)
input() 