from random import randint

n = 0
count = 0
while n < 1000:
	n += 1
    
	d1 = randint(1,6)
	d2 = randint(1,6)
	d3 = randint(1,6)
	d4 = randint(1,6)
	d5 = randint(1,6)
	if d1==d2==d3==d4==d5:
		count += 1
print("The simulation of 1000 times:")
print("The probability of rolling a Yahtzee ", count,
      "The percentage is ","{:.1f}".format((count/1000)*100),"%")  