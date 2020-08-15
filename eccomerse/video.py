import random
import time
from math import *

def f(n):
    if n == 0:
        return 1

    else:
        return n * f(n-1)

n = int(input("Enter a number: "))
print(f(n))

def t(m):
    if m == 0:
        return 1

    else:
        return m + t(m - 1) * 10

m = int(input("Enter a number: "))
print(t(m))

def e(b):
    if b == 0:
        return 1
    else:
        return b + e(b - 5)
b = int(input("Enter a number: "))
print(e(b))


def range(r):
    if r == 0:
        print("nothing")

    elif r > 1 and r < 100:
        print("Within the range")

    elif r < 1 and r > 100:
        print("outside of the the range")

    elif r > 100:
        print("outside the range")

    return r

r = int(input("Enter the number within the the range: "))
print(range(r))


def cap(w):
    d = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"]
    u = 0
    y = 0
    for c in w:
        if c.islower() and d[1]:
            u += 1
            print(u)

        elif c.isupper() or d[0]:
            y += 1
            print(y)

        else:
            pass

    return w

print(cap("ejjrncrj"))


def even_num(n):
    r = ["1", "2", "3", "3", "9", "7", "12", "13", "17", "19", "20", "22", "24"]
    for t in n:
        if n == "2":
            print("2", "12", "20", "22", "24")
            print(r)

        elif n == "3" or "odd":
            print("3", "9", "12", "24")
            print(r)

        return n

n = input("Enter 2 or 3: ")
print(even_num(n))


def




















    










































































































































































































































































































































































































































































