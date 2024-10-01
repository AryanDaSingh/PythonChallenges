import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
a=input("What would you like to write?  ")
t.write(a)
t.forward(len(a)*5)
turtle.done()