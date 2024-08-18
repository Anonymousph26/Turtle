import turtle
scr = turtle.Screen()
scr.setup(width=1280, height=720,startx=0,starty=0)
t = turtle.Turtle()
t.shape("turtle")

t.circle(100)
t.left(45)
for i in range(4):
    t.forward(100)
    t.left(90)
t.right(45)
t.penup()
t.goto(0,200)
t.pendown()
t.right(45)
for i in range(4):
    t.forward(100)
    t.right(90)
t.hideturtle()
scr.mainloop()