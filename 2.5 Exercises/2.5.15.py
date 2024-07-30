# written by Antonenko Igor

"""
Run the programm using py.exe.
Output of IDLE Shell 3.11.4 is incorrect.

"""
height = eval(input("How height is a letter A?: "))
print(" "*(height)+" * ")
for i in range(int(height/1.4)-1):
	print(" "*(height-i)+"*" +" "*(i*2)+ " *", )
print(" "*((height-i)-1)+ "*"*5+"*"*(i*2))
for i in range(int((height/1.4)-1) + 1, height-1):
	print(" "*(height-i)+"*" +" "*(i*2)+ " *",)
input() 