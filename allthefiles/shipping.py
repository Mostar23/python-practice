import eccomerse.video as vnp

import random

print("Hangman man")
print("clue: Something people of the past used")
support = "people of the past used it"
p1 = vnp.letter("Guess a letter: ")
secret_word = "sword"

if p1 == "s":
    print("s____")

elif p1 == "w":
    print("_w___")

elif p1 == "o":
    print("__o___")

elif p1 == "r":
    print("___r_")

elif p1 == "d":
    print("____d")

while p1 == "sword":
    print("You have guessed correctly well done")
    break

while p1 == "d o" or "s w" or "r d" or "":
    print("you are wrong")
    break





















































































        






