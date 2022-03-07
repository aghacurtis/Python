
from random import randint
  
player = input('rock (r), paper (p) or scissors (s)?')

if player == 'r':
  print('you chose rock', end=' ')
  
elif player == 'p':
  print(' you chose paper', end=' ')
  
elif player == 's':
  print('you chose scissors', end=' ')
  
else:
  print('??')
  
print('and the computer chose', end=' ')

chosen = randint(1,3)

if chosen == 1 :
  computer = 'r'
  print('rock')
  
elif chosen == 2 :
  computer = 'p'
  print('paper')
  
else:
  computer = 's'
  print('scissors')

if player == computer:
  print('DRAW!')
  
elif player == 'r' and computer == 's':
  print('Player wins!')
  
elif player == 'r' and computer == 'p':
  print('Computer wins!')
  
elif player == 'p' and computer == 'r':
  print('Player wins!')
  
elif player == 'p' and computer == 's':
  print('Computer wins!')

elif player == 's' and computer == 'p':
  print('Player wins!')
  
elif player == "s" and computer == 'r':
  print('Computer wins!')

else:
  print('Huh?')