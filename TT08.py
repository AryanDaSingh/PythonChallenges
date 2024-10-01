import turtle
t=turtle.Turtle()
t.speed(0)
t.width(3)
t.shape("turtle")
t.pu()
t.goto(-200,200)
t.pd()

def gridBox(s):
    for i in range(4):
        t.fd(s)
        t.lt(90)
for y in range(10):
    for x in range(10):
        gridBox(50)
        t.fd(50)
    t.pu()
    t.bk(500)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.pd()
turtle.done()