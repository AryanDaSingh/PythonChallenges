a=int(input("Which excersize would you like, 1 or 2?    "))
if a==1:
    IgyeomParkBorn = 2010
    MyAge = int(input('When were you born?'))
    AgeDifference = MyAge - IgyeomParkBorn
    print("Igyeom Park is",AgeDifference,"years older than you")
elif a==2:
    celeb=input("Which celebrity would you like to compare your age to")
    celebAge=int(input("which year was your celebrity born in"))
    MyAgeA=int(input("When were you born"))
    AgeDiff=MyAgeA-celebAge
    print(celeb,"is",AgeDiff,"years older than you")