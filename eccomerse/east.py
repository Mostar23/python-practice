import random

import time

import eccomerse.south as st

stz = st.sentence("Enter a sentence: ")

alphabet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
a = random.shuffle(alphabet)

if stz == "":
    print(time.sleep(0.5))
    print(a)
    if stz and a != dict:
        print("you have made a mistake in spelljng")

elif stz and a == "".lower() or "".upper():
    print(a)
    print("you have made a mistake")

else:
    print("Invalid input")




























































































