import turtle as t

t.bgcolor("black")
t.pencolor("white")
t.width(25)
t.penup()
t.goto(160, -100)
t.pendown()
t.left(90)
for i in range(4):
    t.forward(250)
    t.circle(34, 90)
t.penup()
t.goto(85, 30)
t.pendown()
t.circle(80, 360)
t.penup()
t.goto(110, 130)
t.pendown()
t.circle(7, 360)
t.mainloop()
