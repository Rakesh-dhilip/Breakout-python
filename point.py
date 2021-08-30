from turtle import Turtle
class Point(Turtle):
    def __init__(self):
        super().__init__()
        self.point=0
        self.penup()
        self.color("white")
        self.goto((0,-300))
        self.write(f"Score {self.point}", align="center", font=("Verdana", 15, "normal"))
        self.hideturtle()


    def addpoint(self):
        self.point = self.point+1
        self.clear()
        self.write(f"Score {self.point}", align="center", font=("Verdana", 15, "normal"))

    def gameover(self):

        self.clear()
        self.write(f"Score {self.point} and GAMEOVER!!!", align="center", font=("Verdana", 15, "normal"))