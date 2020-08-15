import random
from math import *
import time

print("This programme would take a word and shuffle it")

name = input("Enter a word: ")
space = 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9
n2 = random.sample(name, space)

def convert():
    if name == "" or "1":
        print(name)
        while name == name:
            print(n2)
            print("".join(random.shuffle(n2)))
            break


if name == "" or "1":
    print(convert())

else:
    print("Invalid input")



















































































