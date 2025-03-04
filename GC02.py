hours = int(input())
minutes = str(input())
ampm = input()
if ampm == "pm":
    hours+=12
    print(str(hours) + ":" + minutes)
else:
    print(str(hours) + ":" + minutes)
