class Converter:
	
	def __init__(self,length,unit):
		self.length = length
		self.unit = unit

	def transform(self, unit_transform):
		unit_list = ["inches","feet","yards","miles","kilometrs","meters",\
		"centimetrs","millimetrs"]
		value_in_foot = [12,1,1/3,1/5280,1/3281,1/3.281,1/30.48,1/304.8]
		if unit_transform in unit_list:
			length_transform = round(self.length*value_in_foot[unit_list.index(
				                     unit_transform)]/value_in_foot
				                     [unit_list.index(self.unit)], 6)
		return f"{length_transform} {unit_transform}"

	def inches(self):
		return self.transform("inches")
	def feet(self):
		return self.transform("feet")
	def yards(self):
		return self.transform("yards")
	def miles(self):
		return self.transform("miles")
	def kilometrs(self):
		return self.transform("kilometrs")
	def meters(self):
		return self.transform("meters")
	def centimetrs(self):
		return self.transform("centimetrs")
	def millimetrs(self):
		return self.transform("millimetrs")
c = Converter(9,"inches")
print(c.inches())
print(c.feet())
print(c.millimetrs()) 