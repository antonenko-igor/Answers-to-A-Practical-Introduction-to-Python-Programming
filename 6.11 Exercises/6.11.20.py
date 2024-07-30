print("Pacific - 0, Mountain - 1, Central - 2, Eastern - 3")
time = input("Enter the time (in format 00:00 pm or am) - ")
start_zone = eval(input("Starting zone(the appropriate number) - "))
end_zone = eval(input("Ending zone(the appropriate number) - "))
time_parts = time.split(":")
hours = int(time_parts[0])
minutes = time_parts[1][:-2]
hour_difference = end_zone - start_zone
new_hours = (hours + hour_difference) % 12

if (hours + hour_difference) >= 12:
	if time_parts[1][-2:] == "pm":
		minutes = minutes + "am"
	elif time_parts[1][-2:] == "am":
		minutes = minutes + "pm"
else:
	if time_parts[1][-2:] == "pm":
		minutes = minutes + "pm"
	elif time_parts[1][-2:] == "am":
		minutes = minutes + "am"
print(f"{new_hours}:{minutes}") 