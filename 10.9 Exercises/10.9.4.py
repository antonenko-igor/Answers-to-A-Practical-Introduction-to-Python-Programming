""" В IDLE Shell 3.11.4 the format() operator does not work correctly. 
Run the program in py.exe"""

Prod = ["Apple","Pear","Orange","Strawberry","Plum","Apricot",
"Pineapple","Cherry","Grape","Gooseberry"]
Price = [12.36,45.78,112.12,125.32,69.14,47.65,82.36,72.18,54.95,173.54]
for i in range(10):
	print('{:12s} {:s} {:6.2f}'.format(Prod[i],'$', (Price[i]/1.11)))
	
input() 