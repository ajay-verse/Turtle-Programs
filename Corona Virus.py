import turtle as t

t.pencolor("red")
t.bgcolor("black")
t.penup()
t.goto(0, 200)
t.pendown()
a = 0
b = 0
t.speed(0)
while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    t.hideturtle()
t.mainloop()
