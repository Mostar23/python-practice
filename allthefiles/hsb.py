import random

print("please type begin or start")
buyer = input("customer: ")


if buyer == "begin" or "start":
  print("Thank you lets begin")

print("please type kitchen utensils or kitchen stuff or anything else")
buyer = input("What do you like to buy the best prices for: ")

if buyer == "kitchen utensils" or "Kitchen stuff" or "":
    print("please choose a number for either question one or two")


print("type enter to carry on")
enter = input("type enter: ")

if enter == "enter":
    print("first question")

customer = input("What is your name ? : ")

while customer[0] == "" or "mohamed" or "john" or "james" or "david":
     print("Thank you ")
     break


print("press enter again")
enter2 = input("type enter: ")

if enter2 == "enter":
    print("lets get it started")

customer_income = [input("What is your monthly income ? : ")]

if customer_income[0] == "£1000 - £1500":
    print("We will sell you a bundle of kitchen utensils for £1400 and you can pay the rest slowly in the 4 months. "
              " Thank you for choosing us")


elif customer_income[0] == "£2000 - £3000":
        print("You can pay all the of things you need for a brand new kitchen (since you moved in) for £2500 and you can pay the rest in 5 months."
              " Thank you for choosing our services")








































































































































