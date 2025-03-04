exc = int(input("Which challenge:   "))
if exc == 1:
    for i in range(1,101):
        print(i)
elif exc == 2:
    for i in range(0,101):
        if i % 2 == 0:
            print(i)
elif exc == 3:
    for i in range(1000,-1,-10):
        print(i)
