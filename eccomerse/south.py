import random

print("You can type choose in order to choose your own fighters.")
player1 = input("Player1 enter go: ")

fighters = ["ronny", "toby", "john", "justin"]
ra = random.choice(fighters)

fighters2 = ["rocky", "dante", "suushin", "takeda"]
ra2 = random.choice(fighters2)

arena = ["chunin exams", "uchiha district", "second chunin exams", "hyuga district"]
ar = random.choice(arena)

if player1 == "1" or "go" or "":
    print(ra)
    print(ra + " will be your fighter")

player2 = input("Player2 enter go: ")

if player2 == "2" or "go" or "":
    print(ra2)
    print(ra2 + " will be your fighter")

print("Type random for the computer to select an erena for you or choose to choose yourself")

print("If you want the computer to choose for you type random. I you want to choose type choose.")
place = input("Enter arena: ")

if place == "random":
    print(ar)
    print(ar + " will be the place you guys fight")

while place == "choose":
    print("decide where you want to fight")
    choice = input("Where: ")
    print(ar)
    if choice == arena[0]:
        print(arena[0] + " will be the place you fight")

    elif choice == arena[1]:
        print(arena[1] + " will be the place you fight")

    elif choice == arena[2]:
        print(arena[2] + " will be the place you fight")

    elif choice == arena[3]:
        print(arena[3] + " will be the place you fight")

    else:
        print("Invalid input")
        break






























































