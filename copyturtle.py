#libraries 
import turtle
turtle.colormode(255)

#panel
win = turtle.Screen()
w = 700
h = 700
win.setup(width=w, height=h)
turtle.color("orange")

#drawing
turtle.pensize(3)
turtle.pencolor((128, 73, 37))
turtle.up()
turtle.goto(0, -250)
turtle.down()
turtle.circle(250)

turtle.up()
turtle.goto(0, 0)
turtle.down()
turtle.pencolor((52, 153, 235))
turtle.circle(100)

turtle.up()
turtle.goto(100, 50)
turtle.down()

turtle.pencolor((235, 125, 52))
turtle.pensize(2)
turtle.circle(60)

turtle.up()
turtle.goto(-100, -50)
turtle.down()

turtle.circle(70)

turtle.up()
turtle.goto(-100, 200)
turtle.right(45)
turtle.down()

turtle.pencolor((92, 153, 97))
turtle.forward(400)

turtle.up()
turtle.goto(-60, 200)
turtle.down()

turtle.forward(155)

turtle.up()
turtle.goto(-40, -150)
turtle.down()

turtle.left(90)
turtle.forward(175)

turtle.up()
turtle.goto(-20, -150)
turtle.down()

turtle.forward(90)

turtle.up()
turtle.goto(-150,100)
turtle.down()

turtle.right(135)
turtle.forward(250)

turtle.done()
