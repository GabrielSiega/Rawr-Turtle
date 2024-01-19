import turtle

wn = turtle.Screen()
wn.setup(width=400, height=400)
red = turtle.Turtle()

def curve():
    for i in range(200):
        red.right(1)
        red.forward(1)

def heart():
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve()
    red.left(120)
    curve()
    red.forward(112)
    red.end_fill()

heart()
red.ht()

# Move the turtle to the middle of the heart
red.penup()
red.goto(0, -50)
red.pendown()

# Write the text "Rawr" at faster speed
red.speed(1)
red.write("Rawr", font=("Arial", 16, "normal"))

turtle.done()
