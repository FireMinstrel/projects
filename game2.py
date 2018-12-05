import random

CELLS = {(0, 0):"bedroom", (0, 1):"bathroom", (0, 2):"master bedroom",
         (1, 0):"west hallway", (1, 1):"center hallway", (1, 2):"east hallway",
         (2, 0):"living room", (2, 1):"entryway", (2, 2):"kitchen"}

def get_locations():
  start = CELLS[(2, 1)]
  return start
  
  
def move_player(player, move):
  # player = (x, y)
  x, y = player
  
  if move == 'LEFT':
    y -= 1
  elif move == 'RIGHT':
    y += 1
  elif move == 'UP':
    x -= 1
  elif move == 'DOWN':
    x += 1

  return x, y


def get_moves(player):
  moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
  # player = (x, y)
  
  if player[1] == 0:
    moves.remove('LEFT')
  if player[1] == 2:
    moves.remove('RIGHT')
  if player[0] == 0:
    moves.remove('UP')
  if player[0] == 2:
    moves.remove('DOWN')

  return moves


def draw_map(player):
  print(' _ _ _')
  tile = '|{}'
  
  for idx, cell in enumerate(CELLS):
    if idx in [0, 1, 3, 4, 6, 7]:
      if cell == player:
        print(tile.format('X'), end='')
      else:
        print(tile.format('_'), end='')
    else:
      if cell == player:
        print(tile.format('X|'))
      else:
        print(tile.format('_|'))

monster, door, player = get_locations()
print("Welcome to the dungeon!")

while True:
  moves = get_moves(player)
  
  print("You're currently in room {}".format(player))
  
  draw_map(player)
  
  print("You can move {}".format(moves))
  print("Enter QUIT to quit")
  
  move = input("> ")
  move = move.upper()
  
  if move == 'QUIT':
    break
    
  if move in moves:
    player = move_player(player, move)
  else:
    print("** Walls are hard, stop walking into them! **")
    continue
