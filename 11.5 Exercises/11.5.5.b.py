n = eval(input("Enter a number of teams: "))
scores = {}
for i in range(n):
	name = input("Enter a team name: ")
	w = eval(input("A number of wins: "))
	l = eval(input("A number of losses: "))
	scores[name] = [w,l]
w_team = []
for i in scores.values():
	w_team.append(i[0])
print(w_team) 