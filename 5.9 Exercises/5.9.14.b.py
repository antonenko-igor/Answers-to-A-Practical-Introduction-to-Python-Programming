from random import choice

N_doors = int(input("How many doors are (>= 3? "))

wins_change = 0                    
wins_no_change = 0                 
doors = list(range(1, N_doors+1))                     
for K in range(1, 10000): 
    host_pick = choice(doors) 
    player_pick = choice(doors)
    show = choice([i for i in doors if i != host_pick and i != player_pick])
    if host_pick == player_pick:
      wins_no_change += 1
    player_pick = choice([i for i in doors if i != show and i != player_pick])
    if player_pick == host_pick:
      wins_change += 1    
print(f'Wins by not switching {wins_no_change/N_Trials:.2%}')
print(f'Wins by switching {wins_change/N_Trials:.2%}') 