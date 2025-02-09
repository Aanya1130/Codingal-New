import turtle

#screen 
screen = turtle.Screen()
screen.title("Making a square")
screen.bgcolor("LightBlue")
screen.setup(600,600)

#turtle 
square = turtle.Turtle()
square.pensize(5)
square.shape('turtle')
square.color("RosyBrown")

#draw a square
square.forward(200)
square.left(90)
square.forward(200)
square.left(90)
square.forward(200)
square.left(90)
square.forward(200)

square.hideturtle()

turtle.done()