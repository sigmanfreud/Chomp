import random
#20x50 chomp game
#initialize board
init_board = []
for i in range(20):
  j = []
  for iter in range(50):
    j.append('X')
  init_board.append(j)

#---print&move----
def print_out(init_board):
  for i in init_board:
    for j in i:
      print(j, end = '')
    print()
def choose(i,j):
  for x in range(len(init_board)):
    for y in range(len(init_board[0])):
      if x>= i and y>= j:
        init_board[x][y] = '-'
#-------


def play():
  print_out(init_board)
  while init_board[0][0] == 'X':
    print('Make a move.')
    move = input().split()
    i = int(move[0])
    j = int(move[1])
    choose(i,j)
    print_out(init_board)
    if init_board[0][0] != 'X':
      print ('GAME OVER')
      break
    print("Computer's Turn")
    a = random.randint(i,20)
    b = random.randint(j,50) 
    choose(a,b)
    print_out(init_board)
  print('GAME OVER.')

play()
