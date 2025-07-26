import turtle

turtle.Screen().bgcolor("black")
turtle.Screen().setup(500,600)

p = turtle.Turtle()
p.color("blue")
p.pensize("6")
p.shape("turtle")

n= 6

for i in range(n):
    p.forward(100)
    p.right(360/n)

turtle.done()