n = eval(input("Enter a number of teams: "))
scores = {}
for i in range(n):
	name = input("Enter a team name: ")
	w = eval(input("A number of wins: "))
	l = eval(input("A number of losses: "))
	scores[name] = [w,l]
t = input("Enter a team name: ")
print("The team’s winning percentage. ",t," is",(scores[t][0]/sum(scores[t]))*100) 