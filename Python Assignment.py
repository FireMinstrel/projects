import random
import sys
#I had tried to implement a map, but while the map works by itself in a different file on its own, I haven't been able to mix it into the project.
#Most of this code is based off of two YouTube tutorials.  One was by Webucator(I added extra rooms), and the other was by Bryan Tong.
CELLS = [(0, 0), (0, 1), (0, 2),
         (1, 0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2,)]

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        print("You heard rumors about an abandoned, supposedly haunted house.  Guess who's going adventuring...?"
              + "\nWhat??  You didn't bring a flashlight?!  How will you know where to go?!"
              + "\nYou at least know where you started... Guess you'll be bumping into a lot of things...")
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
    print('Use \'n\', \'s\', \'e\', \'w\' to move')
    print('You can\'t see where you need to go, so you might bump into some walls...')
    print('Good luck and have fun!')
    title_screen()

def get_locations(): # Starting points of the necessary entities
  player = CELLS[0]
  return player

def move_player(player, move): # move the player
  x, y = player

  if move == 'w':
    y -= 1
  if move == 'e':
    y += 1
  if move == 'n':
    x -= 1
  if move == 's':
    x += 1

  return x, y

def get_moves(player): # display the moves the player can take
  moves = ['w', 'e', 'n', 's']
  # player = (x, y)

  if player[1] == 0:
    moves.remove('w')
  elif player[1] == 2:
    moves.remove('e')
  elif player[0] == 2:
    moves.remove('n')
  elif player[0] == 0:
    moves.remove('s')

  return moves

def draw_map(player): # Draws the map
  print(' _ _ _')
  tile = '|{}'

  for spot, cell in enumerate(CELLS):
    if spot in [0, 1, 3, 4, 6, 7]:
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

def msg(room):
    if room['msg'] == '':
        return "You have entered the " + room['name'] + "."
    else:
        return room['msg']

def get_choice(room, dir):
    if dir=='n':
        choice = 0
    elif dir == 'e':
        choice = 1
    elif dir == 's':
        choice = 2
    elif dir == 'w':
        choice = 3
    else:
        return -1

    if room['directions'][choice] == 0:
        return 4
    else:
        return choice

def main():
    dirs = (0, 0, 0, 0) #default

    entrance = {'name':'entryway', 'directions':dirs, 'msg':'', 'position': CELLS[0]}
    l_room= {'name':'living room', 'directions':dirs, 'msg':'', 'position': CELLS[1]}
    kitch= {'name':'kitchen', 'directions':dirs, 'msg':'', 'position': CELLS[2]}
    hall_1= {'name':'hallway', 'directions':dirs, 'msg':'', 'position': CELLS[3]}
    hall_2= {'name':'hallway', 'directions':dirs, 'msg':'', 'position': CELLS[4]}
    hall_3= {'name':'hallway', 'directions':dirs, 'msg':'', 'position': CELLS[5]}
    b_room= {'name':'bedroom', 'directions':dirs, 'msg':'', 'position': CELLS[6]}
    bath= {'name':'bathroom', 'directions':dirs, 'msg':'', 'position': CELLS[7]}
    master= {'name':'master bedroom', 'directions':dirs, 'msg':'', 'position': CELLS[8]}

    #N, E, S, W
    entrance['directions'] = (0, l_room, hall_1, 0)
    l_room['directions'] = (0, kitch, hall_2, entrance)
    kitch['directions'] = (0, 0, hall_3, l_room)
    hall_1['directions'] = (entrance, hall_2, b_room, 0)
    hall_2['directions'] = (l_room, hall_3, bath, hall_1)
    hall_3['directions'] = (kitch, 0, master, hall_2)
    b_room['directions'] = (hall_1, 0, 0, 0)
    bath['directions'] = (hall_2, 0, 0, 0)
    master['directions'] = (hall_3, 0, 0, 0)

    rooms = [entrance, l_room, kitch, hall_1, hall_2, hall_3, b_room, bath, master]
    npcRooms = random.choice(rooms) #there are no NPCs, but I left this variable for future functions I plan to add to this game
    treasure_found = False
    room = entrance
    
    while True:
        draw_map(player)
        if treasure_found and room['name'] == 'entryway':
            print("Congratulations! You have solved the puzzles and found the treasure!\nNow go sell it on eBay!"
                  + "Also, that house wasn't haunted...bummer.  "
                  + "\nTHE END")
            sys.exit()
        elif not treasure_found and room['name'] == 'master bedroom':
            treasure_found = True
            print(msg(room)+ "You see a box in the corner. You walk over to it and open it.  TREASURE!"
                  + "You grab the box.  The treasure is now yours!")
            room['msg'] = ("You are back in the " + room['name'] + ".")
        else:
            print(msg(room))
            room['msg'] = ('You are back in the ' + room['name'])

        stuck = True
        while stuck:
            dir = input("Where do you want to go?(type 'n', 'e', 's', 'w')")
            choice = get_choice(room,dir)
            if choice == -1:
                print("Nope. 'n', 'e', 's', 'w'.  Nothing else.")
            elif choice == 4:
                print("You can't go that way.")
            else:
                room = room['directions'][choice]
                stuck = False


title_screen()                
main()
