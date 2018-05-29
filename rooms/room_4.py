import adventure_game.my_utils as utils

# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms
room4_description = '''
    . . .  4th room ...
     You are in yet another blank room with soft blue walls.
      There are doors to the south and north.
    '''
room4_interacts = {

}
room4_inventory = {

}

def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room4_description)

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
        the_command = response[0
        ]

        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == 'north':
                next_room = 3
                done_with_room = True
            elif go_where == 'south':
                next_room = 5
                done_with_room = True
            else:
                print("Can't go", go_where)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, room4_inventory, take_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room4_inventory, room4_interacts)
        elif the_command == 'drop':
            response = utils.scrub_response(response)
            drop_what = response[1]
            utils.drop_item(player_inventory, room4_inventory, drop_what)
        elif the_command == 'help':
            print("The valid commands are", commands, no_args, )
        else:
            print("that command is not supported yet")
    # END of WHILE LOOP
    return next_room
