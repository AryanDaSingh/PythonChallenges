import turtle
import time

screen = turtle.Screen()
screen.title("Turtle Setup")
screen.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed(0)
t.width(3)

for i in range(4):
    t.fd(100)
    t.lt(90)

time.sleep(3)
t.clear()

turtle.done()
