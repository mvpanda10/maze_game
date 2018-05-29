import adventure_game.my_utils as utils

# # # # #
# ROOM 13
#
# Serves as a good template for blank rooms
room13_bright_description = '''
    . . .  Janitor's Closet ... 
    The closet is dark and littered with cleaning supplies.
    The only light comes from your flashlight.
    In the corner you can see the metal frame 
    of a LADDER gleaming in the bright white light
    '''
room13_dark_description = '''
    The small closet is dark and muggy. There is no light source easily visible...
    well, nothing is visible at all...
    '''
room_state ={
    'dark': True
}
room13_interacts = {

}
room13_inventory = {
    'ladder': 1

}


def run_room(player_inventory):
    # Let the user know what the room looks like
    if room_state['dark']:
        print(room13_dark_description)
    else:
        print(room13_bright_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if room_state['dark']:
            if the_command == 'use':
                response = utils.scrub_response(response)
                use_what = response[1]
                if utils.has_a(player_inventory, use_what):
                    if use_what == 'flashlight':
                        room_state['dark'] = False
                        print("You turn on your flashlight and the room fills with bright white light.")
                        print(room13_bright_description)
                    else:
                        print("You can't use that in this room")
                else:
                    print("You can't use what you don't have!")
            elif the_command == "status":
                print(room13_dark_description)
            elif the_command == 'go':
                response = utils.scrub_response(response)
                direction = response[1]
                if direction == 'west':
                    next_room = 5
                    done_with_room = True
                else:
                    print("There is nowhere to go besides west")
            elif the_command == 'help':
                print("The valid commands are go, help, status, and use, at least until the room is lit.")
            else:
                print("There is nothing else to do in this room until it is lit")

        # now deal with the command
        else:
            if the_command == 'go':
                go_where = response[1].lower()
                if go_where == 'west':
                    next_room = 5
                    done_with_room = True
                else:
                    print("Can't go", go_where)
            elif the_command == 'take':
                response = utils.scrub_response(response)
                take_what = response[1]
                utils.take_item(player_inventory, room13_inventory, take_what)
            elif the_command == 'status':
                utils.player_status(player_inventory)
                utils.room_status(room13_inventory, room13_interacts)
            elif the_command == 'drop':
                response = utils.scrub_response(response)
                drop_what = response[1]
                utils.drop_item(player_inventory, room13_inventory, drop_what)
            elif the_command == 'help':
                print("The valid commands are", commands, no_args, )
            else:
                print("that command is not supported yet")
    # END of WHILE LOOP
    return next_room
