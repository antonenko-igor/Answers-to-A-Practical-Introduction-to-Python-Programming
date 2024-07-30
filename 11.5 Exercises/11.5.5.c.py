n = eval(input("Enter a number of teams: "))
scores = {}
for i in range(n):
	name = input("Enter a name team: ")
	w = eval(input("A number of wins: "))
	l = eval(input("A number of losses: "))
	scores[name] = [w,l]
w_rec = []
for i in scores:
	if scores[i][0] > 0:
		w_rec.append(i)
print(w_rec) 