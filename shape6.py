import turtle
import random
scr = turtle.Screen()
pen = turtle.Turtle()
scr.setup(width=1280,height=720,startx=0,starty=0)
distance = 100
position = []
colors = ["violet", "brown", "blue", "red"]
color1 = random.choice(colors)
pen.speed(0)
pen.penup()
for i in range(8):
    pen.forward(distance)
    pen.dot(5)
    position.append(pen.pos())
    pen.back(distance)
    pen.left(45)
position.append(position[0])
position.append(position[1])
print(position)

for i in range(8):
    pen.pencolor(color1)
    pen.goto(position[i])
    pen.pendown()
    pen.goto(position[i+2])
    pen.penup()
        
    
scr.mainloop()