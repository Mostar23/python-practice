import random
import time

def add(n, m):
    return [n + m]

print(add(8, 9))


def kent(n):
    return n + "you"

print(kent("yess "))


def boss(y):
    return [ch for ch in y]

co = input("place a word in here: ")
ceo = co.join(random.choice(co))

print("word: ", co)
print("shuffling....")
print(boss(ceo))


def letter(u):
    return [ch for ch in u]

wd = input("Enter a word: ")
wdr = wd.join(random.choice(wd))

if wdr == "":
    print(sorted(wdr))

print("word: ", wd)
print("shuffling")
print(letter(wdr))


def sultan(p):
    return [ch for ch in p]

r = input("Enter a word: ")
rz = r.join(sorted(r))

print("word: ", r)
print("sorting...")
print(sultan(rz))

def crossword(u):
    return [ch for ch in u]

name = input("Enter a name: ")

q1 = input("Whats city is the capital of the Uk: ")

word = "[][][][][][]"

print(crossword(q1))

print("checking...")

if q1 in "L" or "l" and q1 not in ["o", "n", "d", "o", "n"]:
    print("L[][][][][]")
    print("Well done", name)

elif q1 in "o" or "O" and q1 not in ["l", "o", "n", "d", "o", "n"]:
    print("[]o[][]o[]")
    print("well done", name)

elif q1 in "n" or "N" and q1 not in ["l", "o", "d", "o"]:
    print("[][]n[][]n")
    print("well done", name)


elif q1 in "d" or "N" and q1 not in ["l", "o", "n", "o", "n"]:
    print("[][][]d[][]")
    print("well done ", name)

elif q1 in "London":
    print("London")
    print("Well done", name, "you win!!")

elif q1 in "l" or "o" "n" and q1 not in ["d", "o", "n"]:
    print("Lon[][][]")
    print("you are half way there")














































































































































































































































