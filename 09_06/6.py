from turtle import *


k = 10
tracer(False)
pendown()
for i in range(3):
    forward(7 * k)
    right(90)
forward(10 * k)
for i in range(3):
    left(90)
    forward(6 * k)
penup()
color('RED')
for y in range(-10, 10):
    for x in range(-10, 10):
        goto(x * k, y * k)
        dot(5)

exitonclick()