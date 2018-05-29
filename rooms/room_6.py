import adventure_game.my_utils as utils

# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms
room6_description = '''
    . . .  6th room ... 
    Another room with blank bright white walls. In the corner, however, there lies a sink.
    The faucet is running and there appear to be no knobs or clamps to control the flow.
    To the EAST and West there are blank white doors with small glass windows. To the 
    SOUTH there is a SIGN with small writing and arrows pointing both ways.
    '''
exam_objs = ['East Door', 'West Door', 'Sign']
sign_description = '''
    The SIGN shows an arrow to the EAST accompanied by the word ELEVATOR and
    an arrow to the WEST accompanied by the words BOSS' OFFICE
    '''
east_door_description = '''
    Through the small glass panel you can see smoke filling the
    room to the EAST. There is too much smoke to possibly breathe in that room
    '''
west_door_description = '''
    Through the small glass panel you can not see much, but you do see a glass case
    with red writing above it. There is also an abstract painting on the NORTHERN wall.
    '''
room6_interacts = {
    'sink': 1,
    'East Door': 1,
    'West Door': 1,
    'Sign': 1
}
room6_inventory = {

}
room_state = {
    'smoke': True
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room6_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["status", "help"]

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
                next_room = 5
                done_with_room = True
            if direction == 'west':
                next_room = 7
                done_with_room = True
            elif direction == 'east':
                if room_state['smoke']:
                    print("You can't go East, the room is too smokey. You need something to cover your mouth.")
                else:
                    next_room = 10
                    done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            response = utils.scrub_response(response)
            take_what = response[1]
            utils.take_item(player_inventory, room6_inventory, take_what)
        elif the_command == 'status':
            utils.player_status(player_inventory)
            utils.room_status(room6_inventory, room6_interacts)
        elif the_command == 'drop':
            response = utils.scrub_response(response)
            drop_what = response[1]
            utils.drop_item(player_inventory, room6_inventory, drop_what)
        elif the_command == 'use':
            response = utils.scrub_response(response)
            use_what = response [1]
            if use_what in player_inventory:
                if use_what == 'rag':
                    utils.use_item(player_inventory, use_what)
                    print("You hold the rag under the running water.")
                    utils.add_item_to_inventory('wet rag', player_inventory)
                elif use_what == 'mug':
                    utils.use_item(player_inventory, use_what)
                    print("The mug fills quickly with cloudy water from the sink")
                    utils.add_item_to_inventory('filled mug', player_inventory)
                elif use_what == 'wet rag':
                    room_state['smoke'] = False
                    print("You cover your mouth with the wet rag.")
            else:
                print("You can't use what you don't have!")
        elif the_command == 'examine':
            response = utils.scrub_response(response)
            exam_what = response[1]
            if exam_what.title() in exam_objs:
                if exam_what == 'Sign':
                    print(sign_description)
                elif exam_what == 'East Door':
                    print(east_door_description)
                elif exam_what == 'West Door':
                    print(west_door_description)
            else:
                print("You can only examine", exam_objs, "in this room")
        elif the_command == 'help':
            print("The valid commands are", commands, no_args, )
        else:
            print("that command is not supported yet")
    # END of WHILE LOOP
    return next_room
