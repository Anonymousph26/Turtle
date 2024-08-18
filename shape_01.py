#####Practice shape #1
##@Serida, Danwen C. 
from turtle import Screen, Turtle
import random

scr = Screen()
scr.setup(width=500, height=500)
tl = Turtle()
tl.pensize(5)
tl.speed(0)
cor = []  
colors = []   


for v in range(200):
    color = ('#' + ''.join(random.choices('0123456789ABCDEF', k=6)))
    colors.append(color)


for i in range(8):
    tl.penup()
    tl.forward(150)
    cor.append(tl.pos()) 
    tl.color(random.choice(colors))  
    tl.dot(5)
    tl.goto(0,0)
    tl.left(45)
    tl.pendown()


x = 0
y = 2
for v in range(6): 
    tl.penup()
    tl.goto(cor[x])
    x += 1
    tl.pendown()
    tl.color(random.choice(colors))
    tl.goto(cor[y])
    y += 1

tx = 6
ty = 0
for b in range(2):
    tl.penup()
    tl.goto(cor[tx])
    tx += 1
    tl.pendown()
    tl.color(random.choice(colors))
    tl.goto(cor[ty])
    ty += 1

scr.mainloop()
