import turtle as t
import os
import binascii
import random 

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


tim.speed("fastest")
def draw(sizeGap):
    for i in range(int(360/sizeGap)):
        tim.color(random_color())
        
        tim.circle(100)
        tim.setheading(tim.heading() + sizeGap)
draw(2)

screen = t.Screen()
screen.exitonclick()