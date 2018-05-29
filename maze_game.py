import sys
import os
import adventure_game.rooms.room_1 as r1
import adventure_game.rooms.room_2 as r2
import adventure_game.rooms.room_3 as r3
import adventure_game.rooms.room_4 as r4
import adventure_game.rooms.room_5 as r5
import adventure_game.rooms.room_6 as r6
import adventure_game.rooms.room_7 as r7
import adventure_game.rooms.room_8 as r8
import adventure_game.rooms.room_9 as r9
import adventure_game.rooms.room_10 as r10
import adventure_game.rooms.room_11 as r11
import adventure_game.rooms.room_12 as r12
import adventure_game.rooms.room_13 as r13
from colorama import init
cwd = os.getcwd()
sys.path.append(cwd + "/./../")
init()


# room imports


# Default the player to the first room
room_number = 1

# Player Inventory
player_inventory = {}

print("Welcome to the maze game...\n")

should_continue = True
while should_continue:
    if room_number == 1:
        room_number = r1.run_room( player_inventory )
    elif room_number == 2:
        room_number = r2.run_room( player_inventory )
    elif room_number == 3:
        room_number = r3.run_room( player_inventory )
    elif room_number == 4:
        room_number = r4.run_room( player_inventory )
    elif room_number == 5:
        room_number = r5.run_room( player_inventory )
    elif room_number == 6:
        room_number = r6.run_room( player_inventory )
    elif room_number == 7:
        room_number = r7.run_room( player_inventory )
    elif room_number == 8:
        room_number = r8.run_room( player_inventory )
    elif room_number == 9:
        room_number = r9.run_room( player_inventory )
    elif room_number == 10:
        room_number = r10.run_room( player_inventory )
    elif room_number == 11:
        room_number = r11.run_room( player_inventory )
    elif room_number == 12:
        room_number = r12.run_room( player_inventory )
    elif room_number == 13:
        room_number = r13.run_room( player_inventory )
    elif room_number == 14:
        print('''
            The elevator begins to slowly rise. As it slows and approaches
            what you can only assume is the 13th floor, the lights flicker.
            Then the elevator stops, the door will not open. You are stuck...''')
        break
    elif room_number == 15:
        print('''
            The elevator begins to descend slowly, then, out of nowhere,
            you hear the cord snap. You begin to fall quickly towards the ground,
            It is obvious there will be no soft ending to this...
            ''')
        break
    else:
        print("Ack I don't know room number:", room_number)
        break
#

print("At least you escaped the maze...")
