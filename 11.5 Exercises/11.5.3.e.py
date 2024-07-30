days = {'january':31, 'february':28, 'march':31, 'april':30,
'may':31, 'june':30, 'july':31, 'august':31,
'september':30, 'oktober':31, 'november':30, 'december':31}

l = list(days.items())

m = input("Enter thr first three letters of the month:  ")

for i in range(len(l)):
    if l[i][0][0:3] == m:
        print("The number of days of the month",l[i][0],"are", l[i][1] )
   
print(l[5][0][0:3]) 