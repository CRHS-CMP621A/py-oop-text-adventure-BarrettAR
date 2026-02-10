from Room import Room

kitchen=Room("Kitchen")
kitchen.set_description("The place where the cooking happens.")

dining_hall=Room('Dining Hall')
dining_hall.set_description('The room where food is consumed.')


ball_room=Room('BallRoom')
ball_room.set_description("Why is it called the ballroom if no balls?")

kitchen.link_room(dining_hall,"south")
dining_hall.link_room(kitchen,"north")
dining_hall.link_room(ball_room,"west")
ball_room.link_room(dining_hall,"east")