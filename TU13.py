e = int(input())
if e == 1:
    num = int(input())
    arr:int = []
    for i in range(num):
        arr.append(int(input()))
    print(sum(arr))
if e == 2:
    num = int(input())
    arr = []
    for i in range(num):
        arr.append(int(input()))
    ave = sum(arr)/len(arr)
    print(sum(arr), min(arr), max(arr), len(arr), ave)
