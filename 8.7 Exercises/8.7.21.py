conversion_rates = [
# into inches,yards,miles, millimeters,centimeters,meters,kilometers
[1, 1/36, 1/63360, 25.4, 2.54, 0.0254, 0.0000254],  # from inches
[36, 1, 1/1760, 914.4, 91.44, 0.9144, 0.0009144],   # from yards
[63360, 1760, 1, 1609344, 160934.4, 1609.344, 1.60934],  # from miles
[0.0393701, 0.00109361, 0.000000621371, 1, 0.1, 0.001, 0.000001],#from millimeters
[0.393701, 0.0109361, 0.00000621371, 10, 1, 0.01, 0.00001],  # from centimeters
[39.3701, 1.09361, 0.000621371, 1000, 100, 1, 0.001],  # from meters
[39370.1, 1093.61, 0.621371, 1000000, 100000, 1000, 1]  # from kilometers
]
length = float(input("Enter a length: "))
from_unit = input("What unit the length is (inches,yards,miles,millimeters,\
	centimeters,meters,kilometers): ")
to_unit = input("What unit you would like to convert(inches, yards, miles,\
 millimeters,centimeters, meters, kilometers): ")
units = ["inches","yards","miles","millimeters","centimeters","meters","kilometers"]
from_index = units.index(from_unit)
to_index = units.index(to_unit)
converted_length = length * conversion_rates[from_index][to_index]
print(f"{length}   is {converted_length} ") 	