import adventure_game.my_utils as utils

room10_interacts = {
    'smokey': True
}
room10_inventory = {

}
# # # # # # # # #
#   Room 2
#       This room can only be gotten too from Room 1
#       You can only go to room 1
#       You can take a key
#       There is nothing to use in this room
#
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop

def run_room(player_inventory):

    room10_description = '''
    . . . 10th Room ...
    The room is filled entirely with smoke. You can barely make out the door to the south. 
    The source of the smoke must be close by.
    '''

    print(room10_description)

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
            if direction == 'west':
                next_room = 6
                done_with_room = True
            elif direction == 'south':
                next_room = 11
                done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, room10_inventory, take_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room10_inventory, room10_interacts)
        elif the_command == 'drop':
            response = utils.scrub_response(response)
            drop_what = response[1]
            utils.drop_item(player_inventory, room10_inventory, drop_what)
        elif the_command == 'help':
            print("The valid commands are", commands, no_args, )
        else:
            print("Command not implemented in ROOM 2,", the_command)

    # end of main while loop
    return next_room
