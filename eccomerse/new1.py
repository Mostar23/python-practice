import random
from math import *
import turtle

name = input("Enter your name: ")

print("h"
     "-"
     "-"
     "k"
     "-"
     "-"
     "-")

def plant(u):
    print("h"
     "-"
     "-"
     "k"
     "-"
     "-"
     "-")

letter = input("Enter a letter: ")

print(plant(name))

if name in "a":
    print("well done!!!", name)
    print("you got one letter right")
    print("h"
          "a"
          "-"
          "k"
          "-"
          "-"
          "-")

elif name in "c":
    print("well done!!!", name)
    print("you got one letter right")
    print("h"
          "-"
          "c"
          "k"
          "-"
          "-"
          "-")


elif name in "k":
    print("well done!!!", name)
    print("you got one letter right")
    print("h"
          "a"
          "c"
          "k"
          "-"
          "-"
          "-")

elif name in "n":
    print("well done!!!", name)
    print("you got one letter right")
    print("h"
          "a"
          "c"
          "k"
          "n"
          "-"
          "-")

elif name in "e":
    print("well done!!!", name)
    print("you got one letter right")
    print("h"
          "a"
          "c"
          "k"
          "n"
          "e"
          "-")

elif name in "y":
    print("well done!!!", name)
    print("you got one letter right")
    print("h"
          "a"
          "c"
          "k"
          "n"
          "e"
          "y")

elif name in "ac":
    print("well done!!", name)
    print("two right yh!")
    print("h"
          "a"
          "c"
          "k"
          "-"
          "-"
          "-")

elif name in "ace":
    print("well done!!", name)
    print("three right yh")
    print("h"
          "a"
          "c"
          "k"
          "-"
          "e"
          "-")

elif name in "acey":
    print("well done!!", name)
    print("four right yh")
    print("h"
          "a"
          "c"
          "k"
          "-"
          "e"
          "y")


elif name in "aceyn":
    print("well done!!", name)
    print("fully correct!!")
    print("h"
          "a"
          "c"
          "k"
          "n"
          "e"
          "y")


elif name in "hackney" or name in "Hackney":
    print("well done!!", name)
    print("fully correct!!")
    print("h"
          "a"
          "c"
          "k"
          "n"
          "e"
          "y")

elif name in "b" or "d" or "f" or "g" or "t" or "j" or "l" or "m" or "o" or "q" or "r" or "s" or "u" or "v" or "w" or "x" or "z":
    print("wrong", name, "come you can do better then this")

else:
    print("Invalid input")


def letter(o):
    return [ch for ch in o]

print("word game 2.3")

new = input("Enter a letter: ")

print("Let the crossword game begin!!", name)


























































