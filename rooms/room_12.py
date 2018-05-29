import adventure_game.my_utils as utils

# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms
room12_description = '''
    . . .  12th room ... 
    It's and elevator. It is apparent that you are on the 
    12th floor. There is a 13th floor you could go to, but there
    is also the option to go down to the ground floor.
    '''
room12_interacts = {

}
room12_inventory = {

}

def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room12_description)

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
        response = utils.ask_command("Go up or down?", commands, no_args)
        the_command = response[0]

        # now deal with the command
        if the_command == 'go':
            go_where = response[1].lower()
            if go_where == 'west':
                next_room = 11
                done_with_room = True
            elif go_where == 'up':
                next_room = 14
                done_with_room = True
            elif go_where == 'down':
                next_room = 15
                done_with_room = True
            else:
                print("Can't go", go_where)
        else:
            print("You can't do that in this room.")
    # END of WHILE LOOP
    return next_room
