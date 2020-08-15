import random
import time
from math import *

print("Welcome to stage games!!")

name = input("Enter your name: ")

print("please wait as we prepare your game for you...")
print(time.sleep(1))

print("Lets start the game " + name)

count = 10

counters = 3

three = 3

limit = 10

out_of_guesses = False

guesses = ""

answer = "George Berkowski"

while guesses != answer and count>0:
  guesses = input("Who is the founder of candy crush " + name + ": ")
  print(f"Your wrote {guesses}")
  count -= 1
  print(count)
  if guesses.strip() == answer:
      print("Correct")
      break
  else:
      print("Wrong")

  #for twenty in answer:
  # if guesses != twenty:
  #    print("wrong", name)
  #    break

while guesses != answer and count == 0:
    hint = input("Would you like a hint: ")
    counters -= 1
    print(counters)
    if hint in ["yes", "yess"] and hint not in ["no", "noo", "n"]:
        print("He's names starts of with G and he is from Australia")
        print("you get no more hints")
        guesses = input("Who is the founder of candy crush " + name + ": ")
        print(f"you wrote {guesses}")
        counters -= 1
        print(counters)
        while guesses.strip() == answer:
            print("Well done!!", name, "you win")
            break

        else:
            print("you lose", name)

    elif hint in "no" or "noo" and hint not in ["yes", "yess"]:
         print("stubborn yh good, keep on going!!")
         guesses = input("Who is the founder of candy crush " + name + ": ")
         print(f"you wrote {guesses}")
         three -= 1
         print(three)
         if guesses.strip() == answer:
             print("Well done!!", name, "you win")
             break

         else:
             print("you lose", name)
             break




prize = ["10 points", "2 hints", "one letter reveal", "a non fiction book of your choice"]
p = random.choice(prize)

print("10 points", " 2 hints", " one letter reveal", " a non fiction book of your choice")

choice = input("Enter shuffle or s to get yourself one of these prizes: ")

if choice == "shuffle" or "s":
    print(name + "you have won " + p)

print("Now " + name + "lets start round 2")










































