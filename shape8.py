import turtle
scr = turtle.Screen()
pen = turtle.Turtle()
long_line = 200
short_line = long_line - 120
dot_size = 5
point1 = []
point2 = []
pen.penup()
pen.speed(0)
for i in range(8):
    pen.forward(long_line)
    pen.dot(dot_size)
    point1.append(pen.pos())
    pen.back(long_line)
    pen.left(45)

pen.left(22.5)
for i in range(8):
    pen.forward(short_line)
    pen.dot(dot_size)
    point2.append(pen.pos())
    pen.back(short_line)
    pen.left(45)
    
point1.append(point1[0])
point2.append(point2[0])
pen.goto(point1[0])
pen.pendown()
pen.begin_fill()
pen.fillcolor('pink')

for i in range(1, 9):
    pen.goto(point2[i-1])
    pen.goto(point1[i])
    
pen.end_fill()
pen.begin_fill()
pen.fillcolor('yellow')

for i in range(9):
    pen.goto(point2[i])
    
pen.end_fill()
scr.mainloop()