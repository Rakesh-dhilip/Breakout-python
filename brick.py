from turtle import Turtle,Screen
class Brick(Turtle):
    def __init__(self,color):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape("square")
        # self.speed(0)
        self.shapesize(stretch_wid=1,stretch_len=3)

    def kill(self):
        self.reset()