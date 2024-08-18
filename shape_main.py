
import turtle
from turtle import Turtle
import random
scr = turtle.Screen()
scr.setup(width=600, height=600)
t = turtle.Turtle()
t.pensize(2)
t.speed(0)
t.shape("turtle")
t.pencolor('blue')

colors=[]
for v in range(100):
    color = ('#' + ''.join(random.choices('0123456789ABCDEF', k=6)))
    colors.append(color)
c = []

# Change the side here !!!
side = 8

angle = 360/side
for i in range(side+2):
    t.penup()
    t.forward(200)
    t.dot(5)
    c.append(t.pos())
    t.goto(0,0)
    t.left(angle)
    t.pendown()  
    
x = 0
y = 1

for i in range(side):
    t.pencolor(random.choice(colors))
    t.goto(0,0)
    t.begin_fill()
    t.fillcolor(random.choice(colors))
    t.goto(c[x])
    x+=1
    t.goto(c[y])
    y+=1
    t.end_fill()
t.goto(0,0)

scr.mainloop()