import turtle
t=turtle.Turtle()
t.speed(0)
t.shape("turtle")
t.pu()
t.goto(-200,-200)
t.pd()
def triangleDraw(n):
    for x in range(n):
        for i in range(3):
            t.fd(30)
            t.lt(360.0/3)
        t.pu()
        t.fd(40)
        t.pd()
for y in range(10):
    triangleDraw(10)
    t.pu()
    t.bk(30*10+10*10)
    t.lt(90)
    t.fd(40)
    t.rt(90)
    t.pd()
turtle.done()