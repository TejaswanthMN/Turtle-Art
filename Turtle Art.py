from turtle import Turtle, Screen, colormode
from random import randint

timmy = Turtle()
screen = Screen()
colormode(255)
timmy.shape("turtle")
timmy.color("coral1")
timmy.speed("fastest")
timmy.penup()
timmy.setpos(-150,-150)
def tl():
    timmy.left(90)
    timmy.penup()
    timmy.forward(50)
    timmy.left(90)
def tr():
    timmy.right(90)
    timmy.penup()
    timmy.forward(50)
    timmy.right(90)

def front():
    timmy.pendown()
    timmy.dot(20,(randint(0,255),randint(0,255),randint(0,255)))
    
    #timmy.forward(10)
for f in range(10):
    front()
    for i in range(10):
        timmy.penup()
        timmy.forward(50)
        front()
    if f%2 == 0:
        tl()
    else:
        tr()


screen.exitonclick()
