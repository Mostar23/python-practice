import eccomerse.video as vs

import random

name = vs.names(input("name: "))
print("Which door do you want to get through door1 and door2")
doorsz = input("which door want to go through: ")
doors = ["door1", "door2"]

if name == "" and doorsz == "1" or "door1" or "one" or doors[0]:
    print(doors[0] + " allows you to enter a room full of sweets and ice cream")
    move = input("steps: ")
    steps = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    if move == steps[3]:
        print("he is at the ice cream machine. he begins to enjoy the ice cream")

    elif move == steps[5]:
        print("He is at the window of the ")

    else:
        print("he begins to enjoy the sweets and video games the room has to offer")

elif name == "" and doorsz == "2" or "two" or doors[1]:
    print(doors[1] + " allows you to enter a room full of sweets and ice cream")
    move2 = input("take some steps: ")
    stepz = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    if move2 == stepz[0]:
        print("You have entered the house")
    elif move2 == stepz[3]:
        print("He observes this room is a gym")

    elif move2 == stepz[6]:
        print("He walks to the running track and start running on it")

    elif move2 == stepz[9]:
        print("He walks to weights section and starts lifting weights")

    else:
        print("he stayed and enjoyed the facilities of the room")

else:
    print("There is something wrong")
































