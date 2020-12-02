import turtle
import random
turtle.setup(800, 600)
turtle.pensize(2)
turtle.pencolor("pink")
turtle.shape("turtle")
turtle.speed(5)
a = 0
for i in range(40):
    turtle.bk(a)
    a += 5
    turtle.left(random.randint(0, 180))
    turtle.fd(a)
turtle.hideturtle()
turtle.done()
