from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(x,y)

    def Left(self):
        if (self.xcor()!=-320):
            self.forward(-40)


    def Right(self):
        if (self.xcor() != 320):
            self.forward(40)