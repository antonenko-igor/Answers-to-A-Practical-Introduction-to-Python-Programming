from random import choice

class Rock_paper_scissors():

	def __init__(self,rounds = 5):
		self.rounds = rounds
		self.current_round = 0
		self.player_wins = 0
		self.computer_wins = 0

	def computer_choice(self):
		choices = ["paper", "rock", "scissors"]
		return choice(choices)

	def find_winner(self,player_choice, computer_choice):
		if player_choice == computer_choice:
			return f"Tie"
		elif (player_choice == "rock" and computer_choice == "scissors") \
		      or (player_choice == "paper" and computer_choice == "rock") \
		      or (player_choice == "scissors" and computer_choice == "paper"):
			self.player_wins += 1
			return f"The player won this round."
		else:
			self.computer_wins += 1
			return f"The computer won this round."

	def check_game_winner(self):
		if self.player_wins == self.computer_wins:
			return f"Tie!"
		elif self.player_wins > self.computer_wins:
			return f"The player won the game!"
		else:
			return f"The computer won the game!"

	def play_round(self,player_choice):
		self.current_round += 1
		computer_choice = self.computer_choice()
		print(f"Round {self.current_round}: The player's choice - {player_choice},\
			The computer's choice - {computer_choice}")

		result = self.find_winner(player_choice, computer_choice)
		print(result)

		if self.current_round == self.rounds:
			game_winner = self.check_game_winner()
			print(game_winner)        	        
game = Rock_paper_scissors(3)
while game.current_round < game.rounds:
	player_choice = input("Your choice from (paper, rock, scissors) - ")
	game.play_round(player_choice) 