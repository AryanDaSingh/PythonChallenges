myHeight=int(input("What is your height in cm (only digits don't write cm)"))
heightComparison=int(input("What is the height of the person you would like to compare your height to"))
if myHeight > heightComparison:
    diff1=myHeight-heightComparison
    print("you are",diff1 + "cm taller")
elif myHeight < heightComparison:
    diff2=heightComparison-myHeight
    print("they are",diff2 + "cm taller")
elif myHeight==heightComparison:
    print("Same height")