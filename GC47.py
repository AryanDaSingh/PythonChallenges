email = input()
arr = list(email)
at = False
pos = -1
before = []
after = []
correctData = False
allowedSymbols = ["!","#","$","%","&","'","*","+","-","/","=","?","^","_","`","{","|","}","~"]
for i in range(len(arr)):
    if arr[i] == '@':
        at = True
        break
    else:
        before.append(arr[i])
        pos = i
for j in range((i+1),len(arr)):
    after.append(arr[j])
if len(before) <= 64:
    for i in range(len(before)):
        # allowed ! # $ % & ' * + - / = ? ^ _ ` { | } ~
        if before[i].isalpha() or before[i].isdigit() or before[i] in allowedSymbols:
            if len(after) <= 253:
                for i in range(len(after)):
                    if after[i].isalpha() or after[i].isdigit() or after[i] in allowedSymbols:
                        correctData = True
if correctData == True:
    print("Success!")
else:
    print("Fail")
