import turtle
from turtle import *
scr = turtle.Screen()
scr.setup(width=1280, height=720, startx=0, starty=0)
t = turtle.Turtle()
speed = 100
t.speed(0)
t.pensize(3)
points = []

for i in range(4):
    points.append(t.pos())
    t.forward(speed)
    t.left(90)

t.home()
for i in range(3):
    t.goto(points[i])
    t.goto(speed / 2, speed)

for i in range(4):
    if i == 2 or 3:
        t.goto(points[i])
    else:
        pass
    
    t.goto(speed / 2, 0)
    


scr.mainloop()
