import time
a = int(input("How long countdown?  "))
for i in range(a):
    print(a)
    a-=1
    time.sleep(1)
print("BLASTOFF!")
