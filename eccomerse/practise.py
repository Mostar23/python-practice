from math import *
import random

class person:
    def __init__(self, name):
        self.name = name

person_list = [
    person("adan"),
    person("ali"),
    person("yousuf")
]

a = [1, 2, 2, 3, 4, 5, 6, 7]
b = ["a", "b", 1, 2]

print(a[0])


#"going through the entire list"
for x in person_list:
    print(x.name)

myresult = [x + 5 for x in a]
print(myresult)

l = [10, 4, 5, 67, 8, 20]
l.sort()

sorted_list = sorted(l)
print(f"sorted_list: {sorted_list}")
print(f'L: {l}')


bee = [2, 4, 5, 6, 2, 7]

my_action = [read + 5 for read in bee]
print(my_action)

my_counter = [incept * 3 for incept in bee]
print(my_counter)

decimals = [0.5, 7.5, 9.0, 2.6, 3.9]

my_decimals = [number for number in decimals]
print(my_decimals)

youtube = [6.8, 3.5, 9.0, 2.4, 6.7]

its_youtube = [forty * 4 * 67 for forty in youtube]
print(its_youtube)

get_away = [900, 567, 344, 190, 100]

is_get_away = [chilling * 67 + 3 for chilling in get_away]
print(is_get_away)

wordz = ["a", "b", "c", "d", "e", "f", "g", "h"]
wordzz = random.choice(wordz)

words = ["faze", "arm", "wrapped", "up"]

is_words = [councel + wordzz for councel in words]
print(is_words)

empires = ["ottomans", "ummayad", "ummyad spain", "abbasids"]

its_empires = [decisive[5] + "z" for decisive in empires]

print(its_empires)

read = ["books", "newspapers", "story", "non fiction"]

its_read = [danger[0] + "n" for danger in read]
print(its_read)


its_read = []
for smart in read:
    its_read.append(smart[2] + "danger")
    its_read.reverse()

print(its_read)


letter = ["b", "a", "w", "a"]

its_letter = [thinking[0] + "reed" for thinking in letter]
print(its_letter)

its_l = random.choice(its_letter)


english = ["open", "tale", "copy", "resliancy"]

it_english = [french + " squad " for french in english]

print(it_english)


list = [
    {
        "king": "ruler",
        "strengh": "software",
        "lancelot": "sir arthur"

    }
]
for thirty in list:
    if list == "king":
        print(list)


number = [11, 90, 45, 89, 30, 67]
number.sort()


numberz = sorted(number)
print(f"sorted number = {numberz}")
print(f"number: {number} ")


readz = ["book", "winter", "front", "break"]
readz.sort()

twizz = sorted(readz)
print(f"sorted in order of the alphabet: {twizz}")
print(f"sorted: {readz}")



numberaz =  [0.6, 5, 90, 20, 0.03]

answer = [year * 3 + 4 * 7 for year in numberaz]
print(answer)

french = ["hide", "sentiment", "words", "hear"]

anton = [again[0] + " it " for again in french]
print(anton)

lx = [1, 7, 5, 9, 4]
lx.sort()

trenches = sorted(lx)
print(f"sorted number: {lx}")
print(f"numbers that are sorted: {trenches}")



hundred = [10, 20, 60, 90, 2987, 346]

h = [vine + 10 for vine in hundred]
print(h)

bz = [10, 20, 60, 90, 2987, 346]
bz.sort()

nz = sorted(bz)
print(f"sorted: {nz}")
print(f"actually sorted: {nz}")

court = [0.78, 43, 2.78, 903, 204, 678, 109]

co = [rent * 10 for rent in court]
print(co)


namew = ["guard", "learn", "pacifist", "underated"]

plot = [air + " ready" for air in namew]
print(plot)



def number():
    numbers = "1234567890"
    n = random.choice(numbers, k=5)
    for thirty in numbers:
        if thirty == str(int):
            print(thirty.join(n))
            if n == "":
                print(numbers)


ent = [12, 56, 78, 90, 34, 56]

chum = [uni * 50 for uni in ent]
print(chum)

wordzzs = ["my ", "two "]

q = [understand + " brother " for understand in wordzzs]
print(q)


jungle = [23, 4, 45, 67, 90, 1, 20, 31]
jungle.sort()

snow = sorted(jungle)
print(f"patterned: {snow}")
print(f"sorted: {jungle}")

alphabet = ["bed", "story", "learn", "air", "otaku"]
alphabet.sort()

print(alphabet)


sony = input("Enter any word an it will sorted alphabetically: ")

def alphabet_sort():
    sony = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    s = random.choice(sony)
    if sony in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        print(s)

listz = [1, 29, 67, 89, 10]

add = [noko + 1289467 for noko in listz]
print(add)

wordzd = ["the ", " my ", "their "]

activity = [alone + "squad" for alone in wordzd]
print(activity)


letterz = ["second", "air", "distance", "meant", "benito"]
letterz.sort()

centermetre = sorted(letterz)
print(f"sorted: {letterz}")
print(f"sorted: {centermetre}")


numerics = [292, 0.67, 900, 1, 4, 67, 98, 20]
numerics.sort()

tool = sorted(numerics)
print(f"sorted: {numerics}")
print(f"sorted: {tool}")


pivitol = ["govener ", "danger ", "books "]
piv = random.choice(pivitol)

territory = [piv + " are around " for victory in pivitol]
print(territory)


written = input("Enter the letter: ")

sentence = "Man love my endz ak"

count = sentence.count(written)

print("string: " + written)
print("checking...")
print("There is ", count, "in the string")


print("I love reading books")

expect = input("Enter a word: ")

se = "I love reading books"

counters = se.count(expect)

print("word: " + se)
print("receiving....")
print("There is ", counters, "in the sentence")


print("reading for is a certi hobby")

r = input("Enter a letter to see how many is in the sentence: ")

st = "reading for is a certi hobby"

territory = st.count(r)

print("amount: ", territory)
print("letter: ", r)
print("counting...")

def splitting(n):
    return [ch for ch in n]

name = input("Enter a name: ")

print("name: ", name)
print("splitting")
print(splitting(name))

def adding(n):
    return [r for r in n]

print("jump on the train")

metrics = input("Enter a letter to take out: ")

practise = "jump on the train"

snow = practise.count(metrics)

print("letter: ", practise)
print("counting...")
print("There is ", snow, " in the sentence")















































































































































































































































































































































