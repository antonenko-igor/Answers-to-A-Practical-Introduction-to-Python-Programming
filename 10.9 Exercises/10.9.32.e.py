from random import choice
M = ["H","T"]
s = "HHTTH"
L = []
for _ in range(100):
	count = 0
	sequence = ""
	while True:
		count += 1
		coin_flip = choice(M)
		sequence += coin_flip
		if len(sequence) >= 5:
			if sequence[-5:] == s:
				L.append(count)
				break
print("the average number of coin flips of the run,like HHTTH, is ", sum(L)/100) 