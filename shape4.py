import turtle
import random
scr = turtle.Screen()
scr.setup(width=1280,height=720,startx=0,starty=0)
ink = turtle.Turtle()
ink.pensize(3)
ink.speed(3)
colors = ['blue', 'red', 'orange', 'violet', 'green']
odd = [1,3,5,7]
even = [0,2,4,6]
loop = [1,2,3,4,5,6,7]
color1 = random.choice(colors)
colors.remove(color1)
color2 = random.choice(colors)
colors.remove(color2)
color3 = random.choice(colors)
angle = 45
long_line = 130
short_line = long_line - 80
position = []

for i in range(9):
    if i in odd:
        ink.pencolor(color1)
        ink.forward(short_line)
        position.append(ink.pos())
        ink.back(short_line)
        ink.left(angle)
    elif i in even:
        ink.pencolor(color2)
        ink.forward(long_line)
        position.append(ink.pos())
        ink.back(long_line)
        ink.left(angle)
ink.penup()
ink.goto(position[0])
ink.pendown()
for i in range(1, 9):
    if i in loop :
        ink.pencolor(color3)
        ink.goto(position[i])
    elif i not in loop:
        ink.goto(position[0])
    
print(position)
        
scr.mainloop()