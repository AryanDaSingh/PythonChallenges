import random

num = random.randint(1,100)
guessMatch:bool = False
while guessMatch == False:
    guess = int(input())
    if guess < 1 or guess > 100:
        print("bro you suck. No play for you")
        break
    if guess == num:
        print("yay")
        guessMatch = True
    elif guess > num:
        print("lower")
    elif guess < num:
        print("higher")
