import adventure_game.my_utils as utils

# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms
room6_description = '''
    . . .  8th room ... 
    In this room there is a ledge. A shiny key lies on top of it.
    '''
room8_interacts = {
    'door_locked' : True
}
room8_inventory = {

}

def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room6_description)

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

        # now deal with the command
        if the_command == 'go':
            direction = response[1].lower()
            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 7
                done_with_room = True
            elif direction == 'east':
                if room8_interacts['door_locked']:
                    print("You can't go East, the door is locked")
                else:
                    next_room = 9
                    done_with_room = True
                    print("You open the door to the east.")
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, room8_inventory, take_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room8_inventory, room8_interacts)
        elif the_command == 'drop':
            response = utils.scrub_response(response)
            drop_what = response[1]
            utils.drop_item(player_inventory, room8_inventory, drop_what)
        elif the_command == 'use':
            response = utils.scrub_response(response)
            use_what = response[1]
            if use_what == 'ladder':
                print("You use the ladder to climb up to the ledge. You grab the key and climb back down")
                utils.add_item_to_inventory('key', player_inventory)
            elif use_what == 'key':
                door_locked = room8_interacts['door_locked']
                if door_locked:
                    room8_interacts['door_locked'] = False
                    print("You unlocked the door to the EAST")
                    utils.use_item(player_inventory, use_what)
                else:
                    print("The door to the EAST is already unlocked")
            else:
                print("You can not use that here")
        elif the_command == 'help':
            print("The valid commands are", commands, no_args, )
        else:
            print("that command is not supported yet")
    # END of WHILE LOOP
    return next_room
