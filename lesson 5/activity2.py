import turtle

#screen 
screen = turtle.Screen()
screen.title("Making a Star")
screen.bgcolor("RosyBrown")
screen.setup(600,600)

#turtle 
star = turtle.Turtle()
star.pensize(7)
star.shape('turtle')
star.color("Brown")

#draw a star

#1st triangle
star.forward(200)
star.left(120)
star.forward(200)
star.left(120)
star.forward(200)
star.left(120)

star.left(90)
star.penup()
star.forward(100)
star.right(90)
star.pendown()

#2nd triangle
star.forward(200)
star.right(120)
star.forward(200)
star.right(120)
star.forward(200)
star.right(120)


turtle.done()