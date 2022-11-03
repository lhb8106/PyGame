# Lab 7 Dr. Roberto Joseph

 

room_list = [] # Empty List

current_room = 0

next_room = 0

 

# N,E,S,W

room = ["You're in Bedroom 2. There is a passage to the east.",3,1,None,None]
room_list.append(room)


room = ["You're in the South Hall",4,2,None,0]
room_list.append(room)


room = ["You're in Dining Room. There is a passage to the west.",5,None,None,1]
room_list.append(room)


room = ["You're in Bedroom 1",None,4,0,None]
room_list.append(room)


room = ["You're in North Hall",6,5,1,3]
room_list.append(room)


room = ["You're in Kitchen",None,None,2,4]
room_list.append(room)


room = ["You're in Balcony",None,None,4,None]
room_list.append(room)

 

done = False
while not done:
    print(' ')
    print(room_list[current_room][0])
    user_input = input('What Direction? ')

    # If user wants to go North
    if user_input.upper() == "N":
        next_room = room_list[current_room][1]
        if next_room == "None":
            print("You can't go that way!")
        else:
            current_room = next_room


    # If user want to go East
    elif user_input.upper() == "E":
        next_room = room_list[current_room][2]
        if next_room == "None":
            print("You can't go that way!")
        else:
            current_room = next_room


    # If user wants to go West
    elif user_input.upper() == "W":
        next_room = room_list[current_room][4]
        if next_room == "None":
            print("You can't go that way!")
        else:
            current_room = next_room


    # If user want to go South
    elif user_input.upper() == "S":
        next_room = room_list[current_room][3]
        if next_room == "None":
            print("You can't go that way!")
        else:
            current_room = next_room


        
    else:
        print('Please try again, I dont understand what you typed')
