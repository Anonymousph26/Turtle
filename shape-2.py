from turtle import Screen, Turtle
import random

scr = Screen()
scr.setup(width=500, height=500)
tl = Turtle()
tl.pensize(3)
cor = []
small_cor = []
colors = []
tl.speed(2)

#this line will generate random colors
for v in range(100):
    color = ('#' + ''.join(random.choices('0123456789ABCDEF', k=6)))
    colors.append(color)
#this line is used to adjust the size of the star
line_1 = 200
line_2 = 80
#this code is for the bone and dots 
for i in range(4): 
    tl.penup()   
    tl.forward(line_1)
    tl.color(random.choice(colors))
    tl.dot(4)
    cor.append(tl.pos()) 
    tl.goto(0, 0)
    tl.left(45)
    tl.forward(line_2)
    tl.color(random.choice(colors))
    tl.dot(4)
    cor.append(tl.pos())
    small_cor.append(tl.pos())
    tl.goto(0, 0)
    tl.left(45)
tl.goto(line_1,0)
tl.pendown()

#this code is responsible for the body of the star body
for i in range(len(cor)):
    tl.color(random.choice(colors))
    tl.goto(cor[i])
    if i == len(cor)-1:
        tl.goto(cor[0])

#this code is responsible for the box in the middle of the star
x = 0
y = 1
for x in range(3):
    tl.color(random.choice(colors))
    tl.goto(small_cor[x])
    x += 1
    tl.goto(small_cor[y])
    y += 1
tl.goto(small_cor[0])

#this code is for the two triangle inside the cube
tx = 1
ty = 0
for b in range(2):
    tl.begin_fill()
    tl.fillcolor(random.choice(colors))
    tl.color(random.choice(colors))
    tl.goto(0,0)
    tl.goto(small_cor[tx])
    tl.end_fill()
    tl.goto(small_cor[ty])
    ty += 2
    tl.goto(small_cor[3])
    tx += 1


scr.exitonclick()