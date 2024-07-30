class Product:
	def __init__(self,name,amount,price):
		self.name = n
		self.amount = a
		self.price = p 

	def get_price(self):
		return f"The regular price - {round(self.amount * self.price, 2)}"

	def make_purchase(self):
		if self.amount < 10:
			return f"The discounted price - {round(a*p, 2)}"

		if self.amount >= 10 and self.amount < 100:
			return f"The discounted price - {round(a * p - (int(a*p*10/100)), 2)}"

		if self.amount > 100:
			return f"The discounted price - {round(a*p - (a*p*20/100), 2)}"

n = input("The product's name: ")
a = eval(input("The number of items of that product: "))
p = eval(input("The regular price: "))

c = Product(n,a,p)
print(c.get_price())
print(c.make_purchase()) 