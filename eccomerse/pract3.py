import random
from math import *

def colours():
    n = ["blue", "brown", "green", "black", "purple"]
    ns = random.choice(n)

    return ns

print(colours())


def three():
    n = input("Enter a word: ")

    if n in "abcdefghijklmnopqrstuvwxyz":
        print(n)

    return print(n[0] or n[2] or n[5])


print(three())


def reverse():
    e = input("Enter a word: ")


    if e in "abcdefghijklmnopqrstuvwxyz":
        print(f"reversed: {e.join(reversed(e))}")

    return e

print(reverse())


def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))






















    

















































