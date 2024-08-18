from turtle import Screen, Turtle
import random

scr = Screen()
scr.setup(width=500, height=500)
tl = Turtle()
tl.pensize(5)
cor = []  #list for the coordinates
colors = []   #list for the random colors

#code to generate random colors
for v in range(200):
    color = ('#' + ''.join(random.choices('0123456789ABCDEF', k=6)))
    colors.append(color)

#this for loop will create the dots
for i in range(8):
    tl.penup()
    tl.forward(150)
    cor.append(tl.pos()) #this line append the coordinates of the dots
    tl.color(random.choice(colors))  #this line will color the dots
    tl.dot(5)
    tl.goto(0,0)
    tl.left(45)
    tl.pendown()

#this code is the list number, the number will increase when it loops 
x = 0
y = 2
for v in range(6): #this for loop is responsible for creating the lines
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

scr.exitonclick()
