import random
import time

Name = input("Enter your name: ")

print("Lets start " + Name)

zero_to_hundred = random.randrange(0, 100, 2)

for intesive in str(zero_to_hundred):
    print(intesive)

user = int(input("Enter a number between 0 to a 100 " + Name + ": "))

time.sleep(0.2)

if user in range(0, 48):
    print("The number is in between 0 and 50")

elif user in range(49, 101):
    print("The number is in between 50 and 100")

else:
    print("Invalid input")

userz = int(input("Enter a number: "))

if userz == userz and (1 or 3 or 5 or 7 or 9):
    print("odd")

else:
    print("even")




























