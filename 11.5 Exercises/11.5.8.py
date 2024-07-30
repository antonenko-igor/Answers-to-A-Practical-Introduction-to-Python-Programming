# "11 - Jack, 12 - Queen, 13 - King, 14 - Ace"
from random import shuffle, randint
suits = ['spades', 'clubs', 'hearts', 'diamonds']
deck = []
deck = [{'value':i, 'suit':c}
for c in suits
for i in range(2,15)]
shuffle(deck)
player1 = []
player2 = []

while True:
    for i in range(3):
        player1.append(deck[randint(2,15)]["value"])
    for i in range(3):
        player2.append(deck[randint(2,15)]["value"])        
    player1.sort()
    player2.sort() 

    if player1 == player2:
        print("Tie")
        break    
    if player1[2] > player2[2]:
        print("Player1 won. Score is",player1[2]," > ",player2[2])
        break
    if player1[2] < player2[2]:
        print("Player2 won.Score is",player1[2]," < ",player2[2])
        break    
    if player1[2] == player2[2]:
        if player1[1] > player2[1]:
            print("Player1 won. Score is",player1[1]," > ",player2[1])
            break       
        if player1[1] < player2[1]:
            print("Player2 won. Score is",player1[1]," < ",player2[1])
            break
            
    if player1[1] == player2[1]:
        if player1[0] > player2[0]:
            print("Player1 won. Score is",player1[0]," > ",player2[0])
            break
        else:
            print("Player2 won. Score is",player1[0]," < ",player2[0])
            break 