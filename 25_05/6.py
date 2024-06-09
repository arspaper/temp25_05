from turtle import *


k = 10
tracer(False)
pendown()
color('RED')
for i in range(2):
    forward(21 * k)
    right(90)
    forward(27 * k)
    right(90)
penup()
forward(9 * k)
right(90)
forward(10 * k)
right(270)
pendown()
for i in range(2):
    forward(86 * k)
    right(90)
    forward(47 * k)
    right(90)
penup()
color('BLACK')
for y in range(-100, 20):
    for x in range(0, 60):
        goto(x * k, y * k)
        dot(5)

exitonclick()


print(18 * 13)