import random
import time
from math import *
import threading

name = input("Enter your name: ")

print(time.sleep(1))

print("Welcome ", name, "lets start the game")


def number(n):
    n = r

count = 0

r = int(input("Enter a number: "))

print("number: ", r)
print("checking...")
if r < 150 and r:
        print("wrong", name, "you have to go higher")
        count += 1

elif r >= 150:
         print("wrong", name, "guess a lower number")
         count += 1
         print(count)

elif r in 150:
         print("Well done", name, "you win!!!")

else:
    print("Invalid input")


def middle_number(x, y, n):
    if x > y and n:
        return x

    elif y > x and n:
        return y

    elif n > y and x:
        return n

print(middle_number(4, 7, 9))


def max_of_2(w, x):

    if w > x:
        return w
    return x

print(max_of_2(32, 33))


def max_of_3(c, d, a):

    if c > d and c > a:
        return c

    elif d > c and d > a:
        return d

    elif a > d and a > c:
        return a

    return d and a

print(max_of_3(67, 78, 90))



def add(n, t, w, i, m):
    return n + t + w + i + m

print(add(8, 5, 6,  7, 9))


def multiply(n, w, t, u):
    return n * t * w * u

print(multiply(8, 9, 6, 7))


sen = "intern"
print(len(sen))

















































































































































