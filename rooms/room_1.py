import adventure_game.my_utils as utils

from colorama import Fore, Style




# # # # # # # # # # # # # # #
#  This is the main room you will start in.
#
#  GO: From this room you can get to Room 2 (SOUTH) and Room 1 (East)
#  Take: There is nothing to take in this room
#  Use: There is nothing to use in this room
#
room_state = {
    'door_locked': True
}
room1_inventory = {}
room1_interacts = {}
def run_room(player_inventory):
    description = '''
    . . . Main Room . . .
    You open your eyes. The room you see is unfamiliar. You see a brightly lit
    doorway to the SOUTH. To the EAST you see a closed door with a lock on it. 

    '''
    print(Fore.BLUE + Style.DIM + description + Style.RESET_ALL)
    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "help"]
    no_args = ["status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1].lower()
            # Use your hand drawn map to help you think about what is valid
            if direction == 'south':
                next_room = 2
                done_with_room = True
            elif direction == 'east':
                if room_state['door_locked']:
                    print("You can't go East, the door is locked")
                else:
                    next_room = 3
                    done_with_room = True
                    print("You open the door to the east.")
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, room1_inventory, take_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room1_inventory, room1_interacts)
        elif the_command == 'drop':
            response = utils.scrub_response(response)
            drop_what = response[1]
            utils.drop_item(player_inventory, room1_inventory, drop_what)
        elif the_command == 'use':
            response = utils.scrub_response(response)
            use_what = response[1]
            if use_what == 'key':
                door_locked = room_state['door_locked']
                if door_locked:
                    room_state['door_locked'] = False
                    print("You unlocked the door to the EAST")
                    utils.use_item(player_inventory, use_what)
                else:
                    print("The door to the EAST is already unlocked")

            else:
                print ("You can not use that here")
        elif the_command == 'help':
            print("The valid commands are", commands, no_args, )
        else:
            print("You can't", the_command, "in this room")
    # end of while loop
    return next_room
