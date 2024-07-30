scores_dict = {}
print("To complete, press - q")
print("Enter game scores in a format like team1 score1 - team2 score2. ")
while True:
	game_score = input(" > ")	
	if game_score == "q":
		break
	L = game_score.split(" ")
	team1 = L[0]
	score1 = L[1]
	team2 = L[3]
	score2 = L[4]
	if team1 not in scores_dict:
		scores_dict[team1] = [0,0]
	if team2 not in scores_dict:
		scores_dict[team2] = [0,0]

	if score1 > score2:
		scores_dict[team1][0] += 1
		scores_dict[team2][1] += 1
	elif score1 < score2:
		scores_dict[team2][0] += 1
		scores_dict[team1][1] += 1
print(scores_dict) 