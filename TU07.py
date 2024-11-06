a = int(input("which excersize: "))
if a == 1:
    for i in range(1,101):
        print(i)
elif a == 2:
    for i in range(1,101):
        if i%2==0:
            print(i)