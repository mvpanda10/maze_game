import adventure_game.my_utils as utils

# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms
room7_description = '''
    . . .  7th room ... 
    There is a PAINTING on the NORTH wall, a glass case that reads
    fire extinguisher, but the glass case is broken. A door to the 
    SOUTH is blocked by a copier.
    '''
room7_no_copier = '''
        . . .  7th room ... 
    There is a PAINTING on the NORTH wall, a glass case that reads
    fire extinguisher, but the glass case is broken.
    '''
exam_objs = ['Painting']
room7_interacts = {
    'Painting': 1,
    'copier': 1
}
painting_description = '''
    You move the painting to the side to expose a small compartment 
    containing a flashlight. You pick it up, it may come in handy.
    '''
room7_inventory = {

}
room_state ={
    'door_blocked' : True,
    'flashlight' : True
}
def run_room(player_inventory):
    # Let the user know what the room looks like
    if room_state['door_blocked']:
        print(room7_description)
    else:
        print(room7_no_copier)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help", "move"]
    no_args = [ "status", "help"]

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
        if room_state['door_blocked']:
            if the_command == 'go':
                go_where = response[1].lower()
                if go_where == 'south':
                    print("The door is blocked by a copier.")
                elif go_where == 'east':
                    next_room = 6
                    done_with_room = True
                else:
                    print("Can't go", go_where)
            elif the_command == 'take':
                response = utils.scrub_response(response)
                take_what = response[1]
                utils.take_item(player_inventory, room7_inventory, take_what)
            elif the_command == 'status':
                utils.player_status(player_inventory)
                utils.room_status(room7_inventory, room7_interacts)
            elif the_command == 'drop':
                response = utils.scrub_response(response)
                drop_what = response[1]
                utils.drop_item(player_inventory, room7_inventory, drop_what)
            elif the_command == 'examine':
                response = utils.scrub_response(response)
                exam_what = response[1].title()
                if exam_what.title() in exam_objs:
                    if room_state['flashlight']:
                        if exam_what == 'Painting':
                            print(painting_description)
                            utils.add_item_to_inventory('flashlight', player_inventory)
                    else:
                        print("You already took the flashlight")
                else:
                    print("You can only examine", exam_objs, "in this room")
            elif the_command == 'move':
                response = utils.scrub_response(response)
                move_what = response[1]
                if move_what.lower() == 'copier':
                    room_state['door_blocked'] = False
                    print("You move the copier out of the way of the door")
                else:
                    print("You can't move", move_what)
            elif the_command == 'help':
                print("The valid commands are", commands, no_args, )
            else:
                print("that command is not supported in this room")
        else:
            if the_command == 'go':
                go_where = response[1].lower()
                if go_where == 'south':
                    next_room = 8
                    done_with_room = True
                elif go_where == 'east':
                    next_room = 6
                    done_with_room = True
                else:
                    print("Can't go", go_where)
            elif the_command == 'take':
                response = utils.scrub_response(response)
                take_what = response[1]
                utils.take_item(player_inventory, room7_inventory, take_what)
            elif the_command == 'status':
                utils.player_status(player_inventory)
                utils.room_status(room7_inventory, room7_interacts)
            elif the_command == 'drop':
                response = utils.scrub_response(response)
                drop_what = response[1]
                utils.drop_item(player_inventory, room7_inventory, drop_what)
            elif the_command == 'examine':
                response = utils.scrub_response(response)
                exam_what = response[1].title()
                if exam_what.title() in exam_objs:
                    if room_state['flashlight']:
                        if exam_what == 'Painting':
                            print(painting_description)
                            utils.add_item_to_inventory('flashlight', player_inventory)
                    else:
                        print("You already took the flashlight")
                else:
                    print("You can only examine", exam_objs, "in this room")
            elif the_command == 'move':
                print("You already moved the copier. There is nothing else to move.")
            elif the_command == 'help':
                print("The valid commands are", commands, no_args, )
            else:
                print("that command is not supported in this room")
    # END of WHILE LOOP
    return next_room
