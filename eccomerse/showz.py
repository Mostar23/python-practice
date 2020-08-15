import time
import random
from math import *

def list_of_benefits():
    print("More organized code", "More readable code", "Easier code")

print(list_of_benefits())


def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "toby")


def my_function2(child3, child2, child1):
    print("The youngest child is " + child1)

print(my_function2(child1="ys", child2="stony", child3="emily"))

def squad4(num1, num2, num3):
    print(num1 + " thought he can beat " + num2 + " in beef but " + num3 + " thought said he would lose")

print(squad4(num1="rondo", num2="la capone", num3="six hunna breezy"))


def my_name(**kid):
    print("His last name is " + kid["fname"])

print(my_function(fname = "Tobias", lname = "Refsnes"))


def my_bits(endz = "Islinghton"):
    print("I am from " + endz)

print(my_bits("Hackney"))
print(my_bits("luton"))
print(my_bits("stepney"))


def my_function4(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

print(my_function4(fruits))


def gujji(clothes):
    for m in clothes:
        print(m)

lane = ["inshallah i will reach sucess"]

print(gujji(lane))


twelve = lambda ar, sq: ar.strip(" * ") + " " + sq.strip(" * ")
print(twelve(" * danger ", " * read "))


read = lambda fn, ln: fn.strip(" * ") + "  " + ln.strip(" * ")
print(read(" Sahid ", " Ahmed"))

print(read(" donetello ", " hajime "))


info = lambda nm, ar: nm.strip(" name ") + " " + ar.strip(" area ")
print(info(" Mohamed ", " Islighton "))


team = lambda nm1, nm2: nm1.strip(" name one ") + " " + nm2.strip(" name two ")
print(team(" squad ", "basketball "))

phone = lambda ph, founder: ph.strip("  ") + " " + founder.strip(" founder ")
print(phone(" iphone ", " steve jobs"))

engineers = lambda eng: eng.strip(" ")
print(engineers(" ibn sina "))

story = lambda rd: rd.strip(" ")
print(story(" the whole squad "))

print(engineers(" ibn sina "))





















































































    















































































































































































































































