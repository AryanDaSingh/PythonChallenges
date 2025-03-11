def defaultLine():
    line(60)
def line(s:int):
    for length in range(1,(s+1)):
        print("|")

#variable
mySize = int(input("How long do you want the line? (-ve will summon defaultLine)  "))

if mySize < 0:
    defaultLine()
else:
    line(mySize)
