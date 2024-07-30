days = {'january':31, 'february':28, 'march':31, 'april':30,
'may':31, 'june':30, 'july':31, 'august':31,
'september':30, 'oktober':31, 'november':30, 'december':31}
items = list(days.items())
print(items)

l = len(items)
for i in range(l-1):
	for j in range(i+1,l):
		if items[i][1]>items[j][1]:
			t = items[i]
			items[i] = items[j]
			items[j] = t 
	sortdays = dict(items)
print(sortdays) 