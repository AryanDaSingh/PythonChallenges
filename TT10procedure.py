import turtle

screen = turtle.Screen()
screen.title("Turtle Setup")
screen.bgcolor("white")
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(0)

def tri(x,y,sz):
    t.pu()
    t.goto(x,y)
    t.pd()
    for i in range(10):
        for i in range(10):
            for i in range(3):
                t.fd(sz)
                t.lt(120)
            t.pu()
            t.fd(sz*2)
            t.pd()
        t.pu()
        t.bk(sz*20)
        t.lt(90)
        t.fd(sz*2)
        t.rt(90)
        t.pd()

tri(-250,-250,10)

turtle.done()
