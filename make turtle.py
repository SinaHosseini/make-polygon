import turtle

turtle.bgcolor("black")
turtle.delay(0)
colors = ["red", "blue", "purple", "green", "yellow", "orange"]

p = turtle.Pen()

i = 0
while i < 270:
    for j in range(len(colors)):
        p.width(i / 75 + 1)
        p.pencolor(colors[j])
        p.forward(i)
        p.left(59)
        i += 1


turtle.done()
