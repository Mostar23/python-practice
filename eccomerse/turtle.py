import turtle
import random
from math import *
from turtle import *
import time

def rand():
    num = ["9", "4", "1", "3", "8", "4", "3", "3", "6", "2", "8", "1", "4", "2"]
    n = random.choice(num)
    print(n)

p1 = input("Enter your name p1: ")

p2 = input("Enter your name p2: ")

print("preparing the game....")

time.sleep(1)

print("Welcome ", p1, "and", p2)

print("[9]", "[4]", "[1]", "[3]", "[8]", "[4]", "[3]", "[3]", "[6]", "[2]", "[8]", "[1]", "[4]", "[2]")

print("here are the  numbers you can use")

print("Verically and horizontally it has to add up to 15")

st = ["-" "|" "-" "|" "-"
      "-" "|" "-" "|" "-"
      "-" "|" "-" "|" "-"]

print("starting from the top left its numbered 1 to 3, second line 4 to 6, third line 7 to 9")

print("use"
      "line (1 or 2 or 3) and s (space) (three paces")

r = input("remember l1 = line 1 and s1 = space 1 !! :) ")

num = ["9", "4", "1", "3", "8", "4", "3", "3", "6", "2", "8", "1", "4", "2"]

box = input("Enter a number " + p1 +": ")

turn = 20

learn = 20

while turn > 0 and learn > 0:
    print(box)
    turn -= 1
    if box in "9 in l1 s1" or "4 in l1 s1" or "1 in l1 s1" or "3 in l1 s1" or "8 in l1 s1" or "4 in l1 s1" or "3 in l1 s1" or "3 in l1 s1" or "6 in l1 s1" or "2 in l1 s1" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
     print(box + "|" "-" "|" "-"
           "-" "|" "-" "|" "-"
           "-" "|" "-" "|" "-")
     print(box)
     print(turn)
     break

    print(num)
    box2 = input("Enter a number" + p2 + ": ")
    learn -= 1
    if box2 in "9 in l1 s1" or "4 in l1 s1" or "1 in l1 s1" or "3 in l1 s1" or "8 in l1 s1" or "4 in l1 s1" or "3 in l1 s1" or "3 in l1 s1" or "6 in l1 s1" or "2 in l1 s1" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
        print(box + "|" "-" "|" "-"
              "-" "|" "-" "|" "-"
              "-" "|" "-" "|" "-")
        print(box2)
        print(learn)
        break




    elif box in "9 in l1 s2" or "4 in l1 s2" or "1 in l1 s2" or "3 in l1 s2" or "8 in l1 s2" or "4 in l1 s2" or "3 in l1 s2" or "3 in l1 s2" or "6 in l1 s2" or "2 in l1 s1" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
     print("-" "|", box, "|" "-"
           "-" "|" "-" "|" "-"
           "-" "|" "-" "|" "-")
     print(box)

     box2 = input("Enter a number"+ p2 +": ")
     if box2 in "9 in l1 s2" or "4 in l1 s2" or "1 in l1 s2" or "3 in l1 s2" or "8 in l1 s2" or "4 in l1 s2" or "3 in l1 s2" or "3 in l1 s2" or "6 in l1 s2" or "2 in l1 s1" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
        print("-" "|",box,"|" "-"
              "-" "|" "-" "|" "-"
              "-" "|" "-" "|" "-")
        print(box2)
        break

     elif box in "9 in l1 s3" or "4 in l1 s3" or "1 in l1 s3" or "3 in l1 s3" or "8 in l1 s3" or "4 in l1 s3" or "3 in l1 s3" or "3 in l1 s3" or "6 in l1 s3" or "2 in l1 s3" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
      print("-" "|" "-" "|", box,
            "-" "|" "-" "|" "-"
            "-" "|" "-" "|" "-")
      print(box)
      break

    box2 = input("Enter a number" + p2 + ": ")
    if box2 in "9 in l1 s3" or "4 in l1 s3" or "1 in l1 s3" or "3 in l1 s3" or "8 in l1 s3" or "4 in l1 s3" or "3 in l1 s3" or "3 in l1 s3" or "6 in l1 s3" or "2 in l1 s3" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
        print("-" "|" "-" "|",box,
              "-" "|" "-" "|" "-"
              "-" "|" "-" "|" "-")
        print(box2)
        break

    elif box in "9 in l2 s1" or "4 in l2 s1" or "1 in l2 s1" or "3 in l2 s1" or "8 in l2 s4" or "4 in l2 s4" or "3 in l2 s1" or "3 in l2 s1" or "6 in l2 s1" or "2 in l2 s1" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
       print("-" "|" "-" "|" "-",
          box,"|" "-" "|" "-"
          "-" "|" "-" "|" "-")
       print(box)
       break

    box2 = input("Enter a number" + p2 + ": ")
    if box2 in "9 in l2 s1" or "4 in l2 s1" or "1 in l2 s1" or "3 in l2 s1" or "8 in l2 s4" or "4 in l2 s4" or "3 in l2 s1" or "3 in l2 s1" or "6 in l2 s1" or "2 in l2 s1" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
        print("-" "|" "-" "|" "-",
              box, "|" "-" "|" "-"
              "-" "|" "-" "|" "-")
        print(box)
        break

    elif box in "9 in l2 s2" or "4 in l2 s2" or "1 in l2 s2" or "3 in l1 s2" or "8 in l2 s2" or "4 in l2 s2" or "3 in l2 s2" or "3 in l2 s2" or "6 in l2 s2" or "2 in l2 s2" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
         print("-" "|" "-" "|" "-"
               "-" "|",box,"|" "-"
               "-" "|" "-" "|" "-")
         print(box)
         break

    box2 = input("Enter a number" + p2 + ": ")
    if box2 in "9 in l2 s2" or "4 in l2 s2" or "1 in l2 s2" or "3 in l1 s2" or "8 in l2 s2" or "4 in l2 s2" or "3 in l2 s2" or "3 in l2 s2" or "6 in l2 s2" or "2 in l2 s2" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
       print("-" "|" "-" "|" "-"
            "-" "|",box,"|" "-"
            "-" "|" "-" "|" "-")
       print(box2)
       break

    elif box in "9 in l2 s3" or "4 in l2 s3" or "1 in l2 s3" or "3 in l1 s3" or "8 in l2 s3" or "4 in l2 s3" or "3 in l2 s3" or "3 in l2 s3" or "6 in l2 s3" or "2 in l2 s3" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
       print("-" "|" "-" "|" "-"
          "-" "|" "-" "|",box,
          "-" "|" "-" "|" "-")
       print(box)
       break

    box2 = input("Enter a number" + p2 + ": ")
    if box2 in "9 in l2 s3" or "4 in l2 s3" or "1 in l2 s3" or "3 in l1 s3" or "8 in l2 s3" or "4 in l2 s3" or "3 in l2 s3" or "3 in l2 s3" or "6 in l2 s3" or "2 in l2 s3" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
        print("-" "|" "-" "|" "-"
              "-" "|" "-" "|",box,
              "-" "|" "-" "|" "-")
        print(box2)
        break


    elif box in "9 in l3 s1" or "4 in l3 s1" or "1 in l3 s1" or "3 in l3 s1" or "8 in l3 s1" or "4 in l3 s1" or "3 in l3 s1" or "3 in l3 s21" or "6 in l3 s1" or "2 in l3 s1" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
     print("-" "|" "-" "|" "-"
          "-" "|" "-" "|" "-",
          box,"|" "-" "|" "-")
     print(box)
     break

    box2 = input("Enter a number"+ p2 +": ")
    if box2 in "9 in l3 s1" or "4 in l3 s1" or "1 in l3 s1" or "3 in l3 s1" or "8 in l3 s1" or "4 in l3 s1" or "3 in l3 s1" or "3 in l3 s21" or "6 in l3 s1" or "2 in l3 s1" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
        print("-" "|" "-" "|" "-"
              "-" "|" "-" "|" "-",
              box, "|" "-" "|" "-")
        print(box2)
        break

    elif box in "9 in l3 s2" or "4 in l3 s2" or "1 in l3 s2" or "3 in l3 s2" or "8 in l3 s2" or "4 in l3 s2" or "3 in l3 s2" or "3 in l3 s2" or "6 in l3 s2" or "2 in l3 s2" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
      print("-" "|" "-" "|" "-"
          "-" "|" "-" "|" "-"
          "-" "|",box,"|" "-")
      print(box)
      break

    box2 = input("Enter a number" + p2 + ": ")
    if box2 in "9 in l3 s2" or "4 in l3 s2" or "1 in l3 s2" or "3 in l3 s2" or "8 in l3 s2" or "4 in l3 s2" or "3 in l3 s2" or "3 in l3 s2" or "6 in l3 s2" or "2 in l3 s2" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
        print("-" "|" "-" "|" "-"
              "-" "|" "-" "|" "-"
              "-" "|",box,"|" "-")
        print(box2)
        break

    elif box in "9 in l3 s3" or "4 in l3 s3" or "1 in l3 s3" or "3 in l3 s3" or "8 in l3 s3" or "4 in l3 s3" or "3 in l3 s3" or "3 in l3 s3" or "6 in l3 s3" or "2 in l3 s3" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
      print("-" "|" "-" "|" "-"
          "-" "|" "-" "|" "-"
          "-" "|" "-" "|",box)
      print(box)
      break
    box2 = input("Enter a number" + p2 + ": ")
    if box2 in "9 in l3 s3" or "4 in l3 s3" or "1 in l3 s3" or "3 in l3 s3" or "8 in l3 s3" or "4 in l3 s3" or "3 in l3 s3" or "3 in l3 s3" or "6 in l3 s3" or "2 in l3 s3" or "8 in l1 s1" or "1 in l1 s1" or "4 in l1 s1" or "2 in l1 s1":
        print("-" "|" "-" "|" "-"
              "-" "|" "-" "|" "-"
              "-" "|" "-" "|",box)
        print(box2)
        break

    while box in ["9 in l3 s3" and "9 in l2 s2" and "9 in l1 s1"] and box2 in [
        "9 in l3 s3" and "9 in l2 s2" and "9 in l1 s1"]:
        print("crossed the line /")
        print("you win!!")
        break

    while box in ["9 in l1 s2" and "9 in l2 s2" and "9 in l3 s2"] and box2 in [
        "9 in l1 s2" and "9 in l2 s2" and "9 in l3 s2"]:
        print("crossed the line /")
        print("you win!!")
        break

    while box in ["9 in l3 s1" and "9 in l2 s2" and "9 in l1 s3"] and box2 in [
        "9 in l3 s1" and "9 in l2 s2" and "9 in l1 s3"]:
        print("crossed the line /")
        print("you win")
        break


if turn == 0 and learn == 0:
    print("end of game")
































































































    






