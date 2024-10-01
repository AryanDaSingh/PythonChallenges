import turtle
colors = ["red","orange","yellow","green","blue","purple","pink","brown","gray","black","white"]
t = turtle.Turtle()
t.width(5)
t.shape("turtle")
t.speed(0)
t.color(colors[1],colors[2])

t.begin_fill()
for i in range(4):
    t.fd(100)
    t.lt(90)
t.end_fill()
turtle.done()