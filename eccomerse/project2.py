import random

print("Enter your name")
student = input("name: ")

if student == "":
    print("lets get it started")

print("Enter the question number")
question = input("question: ")

answer = "1939"
guess_count = 0
guess_limit = 3

q1 = input("When did world war two start: ")

while question == "1" == q1 != ("1939"):
    print("you are wrong")
    attempt2 = input("second try: ")
    guess_count += 1
    if attempt2 != answer:
        print("you are wrong")

    else:
        print("you are correct")

q2 = input("who were the medici: ")

if question == "2" == q2 == "a rich italian family" or "one leading man of florence" or "leaders of florence":
    print("well done")

while question == "2" == input("who were the medici: ") == "a rich italian family" or "one leading man of florence" or "leaders of florence":
    print(" this is correct")
    attempt = input("second try: ")
    if attempt != "a rich italian family" or "one leading man of florence" or "leaders of florence":
     print("you are wrong you don't get anymore chances")

    else:
      print("this is wrong")

















































