from Room import Room
from Item import Item
from Character import *

# egg=Item('Egg')
# egg.set_description('A round white egg')

dave = Enemy("Dave", "A smelly zombie")

kitchen=Room("Kitchen")
kitchen.set_description("The place where the cooking happens.")

dining_hall=Room('Dining Hall')
dining_hall.set_description('The room where food is consumed.')
dining_hall.set_chara(dave)

ball_room=Room('BallRoom')
ball_room.set_description("Why is it called the ballroom if no balls?")

kitchen.link_room(dining_hall,"south")
dining_hall.link_room(kitchen,"north")
dining_hall.link_room(ball_room,"west")
ball_room.link_room(dining_hall,"east")

# dave.set_conversation("I am evil.")
# dave.describe()
# dave.talk()
# dave.set_weakness('Peas')
# print("what will you fight with? ")
# fight_with=input()
# dave.fight(fight_with)

current_room=kitchen
while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_chara()
    if inhabitant is not None:
        print()
        inhabitant.describe()
    command = input("> ")
    current_room = current_room.move(command)