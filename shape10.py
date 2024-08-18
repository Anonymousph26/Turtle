import turtle
import random
pen = turtle.Turtle()
scr = turtle.Screen()
pentagon = 360 / 7
distance = 100
position = []
randcol = []
pen.penup()
pen.speed(0)
pen.pensize(3)

for i in range(7):
    colors = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
    randcol.append(colors)
    

for i in range(7):
    pen.left(pentagon)
    pen.forward(distance)
    pen.dot(5)
    position.append(pen.pos())
    pen.back(distance)
    
position.append(position[0])
pen.pendown()

for i in range(7):
    colors1 = random.choice(randcol)
    pen.begin_fill()
    pen.fillcolor(colors1)
    pen.goto(position[i])
    pen.goto(position[i+1])
    pen.home()
    pen.end_fill()
    randcol.remove(colors1)
    
scr.mainloop()