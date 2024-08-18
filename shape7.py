import turtle
scr = turtle.Screen()
pen = turtle.Turtle()
scr.setup(width=1280,height=720,startx=0,starty=0)
long_distance = 200
short_distance = long_distance / 2
position1 = []
position2 = []
odd = [1,3,5,7]
pen.speed(0)
pen.penup()

for i in range(4):
    pen.forward(long_distance)
    position1.append(pen.pos())
    pen.dot(5)
    pen.back(long_distance)
    pen.left(45)
    pen.forward(short_distance)
    position1.append(pen.pos())
    pen.dot(5)
    pen.back(short_distance)
    pen.left(45)
position1.append(position1[0])
position1.append(position1[1])
pen.goto(position1[0])
pen.pendown()
for i in range(1,10):
    pen.goto(position1[i])
for i in range(1,7):
    if i in odd:
        pen.goto(position1[i+2])
        position2.append(pen.pos())
    else:
        pass

pen.goto(position1[1])
pen.begin_fill()
pen.fillcolor("pink")
pen.home()
pen.goto(position2[0])
pen.end_fill()

pen.goto(position2[1])
pen.begin_fill()
pen.home()
pen.goto(position2[2])
pen.end_fill()
    
    
scr.mainloop()