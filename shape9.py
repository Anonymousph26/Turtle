import turtle
pen = turtle.Turtle()
scr = turtle.Screen()
position = []
position2 = []
sides = 70
line = sides + 32
for i in range(9):
    position.append(pen.pos())
    pen.left(40)
    pen.forward(sides)
print(position)

pen.left(110)
pen.forward(line)
position2.append(pen.pos())

for i in range(1, 9):
    pen.goto(position[i])
    pen.goto(position2[0])
scr.mainloop()