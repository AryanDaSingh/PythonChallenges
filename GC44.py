import turtle
import random

turtle.screensize(1000, 1000, "white")  # Added to make this work on smaller screens
turtle.setup(width=1000, height=800)

r1 = random.randint(20, 700)
t1 = (800 - r1) / 2

r2 = random.randint(20, 700)
t2 = (800 - r2) / 2

r3 = random.randint(20, 700)
t3 = (800 - r3) / 2

r4 = random.randint(20, 700)
t4 = (800 - r4) / 2

r5 = random.randint(20, 700)
t5 = (800 - r5) / 2

r6 = random.randint(20, 700)
t6 = (800 - r6) / 2

r7 = random.randint(20, 700)
t7 = (800 - r7) / 2

r8 = random.randint(20, 700)
t8 = (800 - r8) / 2

r9 = random.randint(20, 700)
t9 = (800 - r9) / 2

randomr = [r1, r2, r3, r4, r5, r6, r7, r8]
randomt = [t1, t2, t3, t4, t5, t6, t7, t8]

turtle.speed(0)
turtle.up()
turtle.goto(-400, 350)
turtle.down()

for i in range(7):
    turtle.forward(randomr[i])
    turtle.up()
    turtle.forward(randomt[i])
    turtle.down()
    turtle.forward(randomt[i])
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(randomr[i])
    turtle.up()
    turtle.forward(randomt[i])
    turtle.down()
    turtle.forward(randomt[i])
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)

turtle.forward(r9)
turtle.up()
turtle.forward(t9)
turtle.down()
turtle.forward(t9)
turtle.left(90)
turtle.forward(800)

turtle.up()
turtle.goto(-400, 380)
turtle.shape("turtle")
turtle.color("red")
turtle.speed(1)
turtle.down()

def move_forward():
    turtle.forward(20)

def move_backward():
    turtle.backward(20)

def turn_left():
    turtle.left(30)

def turn_right():
    turtle.right(30)

turtle.listen()
turtle.onkey(move_forward, "Up")
turtle.onkey(move_backward, "Down")
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")

turtle.done()

#im sorry for doing this