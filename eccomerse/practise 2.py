import random
from math import *

word = input("Enter a word or a sentence: ")

# wrong version
def seperate():
   for w in word:
        if w == "" or "fnjjcem":
         print(list(w.split()))


if word == "":
    print(seperate())

else:
    print("Invalid input")


# right version

def split_str(s):
    return [ch for ch in s]

wordz = input("Enter a word:")

print("string: ", wordz)
print("splitting string...")
print("here its is ")
print(split_str(wordz))


def split(r):
    return [c for c in r]

history = input("Enter any word: ")

print("string: ", history)
print("splitting string...")
print(split(history))

words = input("Enter a word or a sentence: ")

tale = [net + "squad " for net in words]
print(tale)

squad = input("Enter a word: ")

if squad == "" or "cjjd":
    print(len(squad.split()))

count = 0

print("you are a real savage")

enter = input("Enter a word to count: ")


def spliter(n):
    return [ch for ch in n]

read = input("Enter a name: ")

print("namme: ", read)
print("splitting....")
print("splitted: ", spliter(read))


def takeoff(i):
    return [ch for ch in i]

name = input("name: ")
print(name)

print("word: ", name)
print("taking ou the last letter...")
print(takeoff(name[:-1]))


def srtart(n):
    return [ch for ch in n]

word = input("Enter any word: ")

if word[0] in "a" or "b" or "c":
    print(word[0])

else:
    print("Invalid input")










































































































































































