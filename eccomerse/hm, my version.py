import time

name = input("What is your name?:  ")

print(f"Hi {name}, lets start playing the hangman game !!! ")

print(time.sleep(0.5))

secret_word = "mafia"

question = "What is the name of an italian family the deals in crime ?"
print(question)

guessess = input("Enter the guess: ")

guess = 10

if guessess != secret_word:
   for attempt in guessess:
       if attempt not in  ["m" , "a" ,"f" ,"i" ,"a"]:
          print("this letter is not in the secret word")
          print("-")


       elif  attempt in ["m" , "a" ,"f" ,"i" ,"a"]:
           print("you got one letter correct")

       else:
           print("invalid input")



while guessess != secret_word:
    guess -= 1
    if guess <= 10:
     print("try again")
     print("-")
     break

    elif guess == 0:
        print("you win !!!")
        break




























