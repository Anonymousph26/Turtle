
from turtle import Screen, Turtle
import random

scr = Screen()
scr.setup(width=500, height=500)
tl = Turtle()
tl.pensize(5)
angle = 45
cor1 = []
cor2 = []
colors = []
tl.speed(50)


for v in range(100):
    color = ('#' + ''.join(random.choices('0123456789ABCDEF', k=6)))
    colors.append(color)

for i in range(8):
    tl.penup()
    tl.forward(200)
    cor1.append(tl.pos())
    tl.color(random.choice(colors))
    tl.dot(5)
    tl.goto(0,0)
    tl.left(angle)
    tl.pendown()
tl.left(angle / 2)

for n in range(9):
    tl.penup()
    tl.forward(50)
    tl.left(angle)
    cor2.append(tl.pos())
    tl.color(random.choice(colors))
    tl.dot(5)
    tl.goto(0,0)
    tl.pendown()
tl.penup()
tl.goto(cor1[0])
tl.pendown()

x = 0
y = 0
for v in range(8):
    tl.color(random.choice(colors))
    tl.begin_fill()
    tl.fillcolor(random.choice(colors))
    tl.goto(cor1[x])
    x += 1
    tl.goto(cor2[y])
    y += 1
    tl.end_fill()
tl.begin_fill()
tl.fillcolor(random.choice(colors))
tl.goto(cor1[0])
tl.goto(cor2[0])
tl.end_fill()


tl.begin_fill()
tl.fillcolor(random.choice(colors))
for n in range(len(cor2)):
    tl.goto(cor2[n])
tl.end_fill()

scr.mainloop()
#scr.exitonclick()