e = int(input())
if e == 1:
    num = int(input())
    arr = []
    for i in range(num):
        arr.append(str(input()))
    print(arr[0:4])
elif e == 2:
    num = int(input())
    chars = []
    for i in range(num):
        chars.append(str(input()))
else:
    print("Get out")
