import adventure_game.my_utils as utils

room11_interacts = {
    'fire' : True
}
room11_inventory = {

}


# # # # # # # # #
#   Room 2
#       This room can only be gotten too from Room 1
#       You can only go to room 1
#       You can take a key0
#       There is nothing to use in this room
#
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop

def run_room(player_inventory):
    room11_description = '''
    . . . 11th Room ...
    There it is! The ELEVATOR!!! However it is blocked by fire.
    You must use something to 
    '''

    print(room11_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]

        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 10
                done_with_room = True
            if direction == 'east':
                if room11_interacts['fire']:
                    print("You can't walk through fire.")
                else:
                    next_room = 12
                    done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, room11_inventory, take_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room11_inventory, room11_interacts)
        elif the_command == 'drop':
            response = utils.scrub_response(response)
            drop_what = response[1]
            utils.drop_item(player_inventory, room11_inventory, drop_what)
        elif the_command == 'help':
            print("The valid commands are", commands, no_args, )
        elif the_command == 'use':
            response = utils.scrub_response(response)
            use_what = response[1]
            if utils.has_a(player_inventory, use_what):
                if use_what == 'filled mug':
                    room11_interacts['fire'] = False
                    print("You throw the water and extinguish the flame. Now you can leave through the elevator.")
                else:
                    print("You can't use that here.")
            else:
                print("You can't use that here.")
        else:
            print("Command not implemented in ROOM 2,", the_command)

    # end of main while loop
    return next_room
