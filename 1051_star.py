import turtle

turtle.Screen().bgcolor("black")
turtle.Screen().setup(600,700)

p = turtle.Turtle()

p.pencolor("lime")
p.pensize("5")
p.shape("turtle")

p.penup()
p.goto(-110,90)
p.pendown()

for i in range(5):
    p.forward(300)
    p.right(144)

turtle.done()