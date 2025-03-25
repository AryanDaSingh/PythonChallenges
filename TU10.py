import random
e = int(input())
if e == 1:
    print(round(random.uniform(0.1, 9.9), 1))
elif e == 2:
    names = ['James', 'Harry', 'Larry', 'Barry', '성기훈']
    pick = False
    while not pick:
        chosen = random.choice(names)
        print(f"Chosen name: {chosen}")
        a = input("Confirm your choice by typing 'Y': ").strip()
        if a.upper() == "Y":
            pick = True
