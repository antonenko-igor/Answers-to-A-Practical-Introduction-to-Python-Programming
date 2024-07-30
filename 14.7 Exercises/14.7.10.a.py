class Connect4:
	def __init__(self):
		self.board = [[' ' for _ in range(7)] for _ in range(6)]
		self.players = ['X', 'O']
		self.player = 0

	def print_board(self):
	 	for row in self.board:
	 		print("  |  ".join(row) + "  |")
	 		print("-" * 34)
	 	print("    ".join([str(i) for i in range(7)]))
	 	print()
	       		
	def get_spots(self, col):
		if 0 <= col < 7 and self.board[0][col] == ' ':
			for i in range(5, -1, -1):
				if self.board[i][col] == ' ':
					self.board[i][col] = self.players[self.player]
					return True
		return False

	def check_winner(self):
		directions = [(1,0),(0,1),(1,1),(1,-1)]

		for i in range(6):
			for j in range(7):
				if self.board[i][j] != " ":
					for d in directions:
						x, y = i, j 
						count = 0
						while 0 <= x <= 6 and 0 <= y <= 7 and self.board[x][y] \
						== self.board[i][j]:
							count += 1
							x, y = x + d[0], y + d[1]
							if count == 4:
								return True
		return False 