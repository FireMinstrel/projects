import random
import sys

CELLS = {(0, 0):"bedroom", (0, 1):"bathroom", (0, 2):"master bedroom",
         (1, 0):"west hallway", (1, 1):"center hallway", (1, 2):"east hallway",
         (2, 0):"living room", (2, 1):"entryway", (2, 2):"kitchen"}

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        print("You heard rumors about an abandoned, supposedly haunted house.\nThey say there's treasure inside somewhere.\  Guess who's going adventuring...?")
        main()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            main()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    print('######################')
    print('###### Welcome! ######')
    print('######################')
    print('        -Play-        ')
    print('        -Help-        ')
    print('        -Quit-        ')
    title_screen_selections()

def help_menu():
    print('######################')
    print('###### Welcome! ######')
    print('######################')
    print('Use \'n\', \'s\', \'e\', \'w\' to move.')
    print('Good luck and have fun!')
    title_screen()

def get_locations():
  start = CELLS[(2,1)]
  return start
  
  
def move_player(player, move):
  x, y = player
  if move == 'W':
    y -= 1
  elif move == 'E':
    y += 1
  elif move == 'N':
    x -= 1
  elif move == 'S':
    x += 1

  return (x, y)


def get_moves(player):
  moves = ['W', 'E', 'N', 'S']
  # player = (x, y)
  
  if player[1] == 0:
    moves.remove('W')
  if player[1] == 2:
    moves.remove('E')
  if player[0] == 0:
    moves.remove('N')
  if player[0] == 2:
    moves.remove('S')

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

player = get_locations()


def main():
    print("Welcome to the dungeon!")
    treasure_found = False
    player = (2, 1)
    while True:
      moves = get_moves(player)
      
      print("You're currently in the {}".format(CELLS[player]))
      
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
        print("** CRASH! **")
        continue
      if treasure_found and player == (2, 1):
        print("Congratulations! You have solved the puzzles and found the treasure!\nNow go sell it on eBay!"
                  + "Also, that house wasn't haunted...bummer.  "
                  + "\nTHE END")
        sys.exit()
      elif not treasure_found and player == (0, 2):
        treasure_found = True
        print("You see a box in the corner. You walk over to it and open it.  TREASURE!"
                  + "You grab the box.  The treasure is now yours!")
      else:
        continue

title_screen()
main()  
