a=int(input("select activity 1,2,or 3   "))
if a==1:
    test = input("Is it raining? y/n ")
    if test == "y":
        print("Oh dear, no football today!")
    #if you were to make the suggested changes, it would result in a syntax error
elif a==2:
    test = input("Is it raining? y/n ")
    if test == "y" or "yes":
        print("Oh dear, no football today!")
elif a==3:
    test = input("Is it raining? y/n ")
    if test == "y" or "yes":
        print("Oh dear, no football today!")
    elif test=="n" or "no":
        print("Great we can play!")