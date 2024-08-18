import turtle
import random
from turtle import *
scr = turtle.Screen()
scr.setup(width=1280, height=720, startx=0, starty=0)
t = turtle.Turtle()
radius = 100
angle2 = 45
colors = ['blue', 'red', 'orange', "violet", "green"]
odd = [1, 3, 5, 7]
even = [0, 2, 4, 6]
color1 = random.choice(colors)
color2 = random.choice(colors)
t.pensize(3)
t.speed(5)
t.penup()
t.goto(0,-100)
t.pendown()
t.circle(radius)
t.penup()
t.home()
t.pendown()


for i in range(8):
   if i in odd:
      t.pencolor(color1)
      t.forward(radius)
      t.back(radius)
      t.left(angle2)
   if i in even:
      t.pencolor(color2)
      t.forward(radius)
      t.back(radius)
      t.left(angle2)
      

scr.mainloop()