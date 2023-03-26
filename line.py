from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        line = Turtle()
        line.hideturtle()
        line.shapesize()
        line.width(5)
        line.color("white")

        line.penup()    
        line.goto(0,300)
        line.setheading(270)

        for i in range(0,30):
            line.pendown()
            line.forward(10)
            line.penup()
            line.forward(10)
        


