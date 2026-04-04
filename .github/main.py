from Room import Room
from Item import Item
from Character import *

# egg=Item('Egg')
# egg.set_description('A round white egg')

dave = Enemy("Dave", "A smelly zombie")
john_ball_room=Enemy("John BallRoom","Inventor of the Ball Room")

kitchen=Room("Kitchen")
kitchen.set_description("The place where the cooking happens.")

dining_hall=Room('Dining Hall')
dining_hall.set_description('The eating room.')
dining_hall.set_chara(dave)

ball_room=Room('BallRoom')
ball_room.set_description("Why is it called the ballroom if no balls?")
ball_room.set_chara(john_ball_room)

kitchen.link_room(dining_hall,"south")
dining_hall.link_room(kitchen,"north")
dining_hall.link_room(ball_room,"west")
ball_room.link_room(dining_hall,"east")

dave.set_conversation("I am evil.")
dave.set_weakness('peas')

john_ball_room.set_conversation("I am the creator of the Ball Room!")
john_ball_room.set_weakness("balls")

current_room=kitchen
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_chara()
    if inhabitant is not None:
        print()
        inhabitant.describe()
    command = input("> ")
    if command in ["north","south","east","west"]:
        current_room = current_room.move(command)
    elif command == "talk".lower():
        if inhabitant is not None:
            print()
            print(inhabitant.talk())
        elif inhabitant is None:
            print()
            print("There is no one to talk to.")
    elif command == "fight".lower():
        print()
        print("What do you want to fight",inhabitant.name,"with?")
        fight_with=input()
        fight_outcome=inhabitant.fight(fight_with.lower())
        if fight_outcome == False:
            quit()