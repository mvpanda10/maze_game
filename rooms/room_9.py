import adventure_game.my_utils as utils

# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms
room9_description = '''
    . . .  9th room ... 
    This appears to be the boss' office. A large portrait rests
    above the mahogany desk in front of you. Beside the desk you 
    see a rag. behind the desk lies a locked red box. In a partially 
    opened drawer you see the glimmer of a key.
    '''
room9_interacts = {
    'locked_box' : 1
}
box_inventory = {
    'key card': 1
}
room9_inventory = {
    'rag' : 1,
    'key' : 1
}


def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room9_description)

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
            if go_where == 'west':
                next_room = 8
                done_with_room = True
            else:
                print("Can't go", go_where)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, room9_inventory, take_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room9_inventory, room9_interacts)
        elif the_command == 'use':
            response = utils.scrub_response(response)
            use_what = response[1]
            if utils.has_a(player_inventory, use_what):
                if use_what == 'key':
                    print("You approach the box with the key out to unlock it.")
                    utils.use_item(player_inventory, use_what)
                    utils.open_box(box_inventory, player_inventory)
                else:
                    print("You can't use that here.")
            else:
                print("You can't use that here.")
        elif the_command == 'drop':
            response = utils.scrub_response(response)
            drop_what = response[1]
            utils.drop_item(player_inventory, room9_inventory, drop_what)
        elif the_command == 'help':
            print("The valid commands are", commands, no_args, )
        else:
            print("that command is not supported yet")
    # END of WHILE LOOP
    return next_room
