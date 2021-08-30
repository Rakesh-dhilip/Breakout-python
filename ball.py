from turtle import Turtle,Screen
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.shape("circle")
        self.goto(0,-180)
        self.x_move=12
        self.y_move=12

    def move(self):
        x=self.xcor()+self.x_move
        y=self.ycor()+self.y_move
        self.goto(x,y)

    def bounce_Y(self):
        self.y_move=self.y_move*-1

    def bounce_X(self):
        self.x_move=self.x_move*-1

