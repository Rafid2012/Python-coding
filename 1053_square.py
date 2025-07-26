import turtle

turtle.Screen().bgcolor("black")
turtle.Screen().setup(500,600)

p = turtle.Turtle()
p.color("maroon")
p.pensize("3")
p.shape("turtle")

p.penup()
p.goto(-100,75)
p.pendown()

n= 4
for i in range(n):
    p.forward(180)
    p.right(90)

turtle.done()