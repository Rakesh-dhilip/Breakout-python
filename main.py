import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from point import Point
import random
color=["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
ball = Ball()
screen.tracer(0)
screen.bgcolor("black")
screen.setup()
paddle = Paddle(0, -200)
screen.listen()
screen.onkey(paddle.Left,"Left")
screen.onkey(paddle.Right,"Right")
bricks=[]
point=Point()
y=300
for j in range(4):
    x = -340
    for i in range(11):
        brick = Brick(random.choice(color))
        brick.goto(x,y)
        x=x+65
        bricks.append(brick)

    y=y-50

gameon = True
while gameon:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if (ball.xcor()>340 or ball.xcor() < -340):
        ball.bounce_X()

    if (ball.ycor()>320):
        ball.bounce_Y()

    if(paddle.distance(ball)<30):
        ball.bounce_Y()

    if (ball.ycor() < -320):
        gameon=False
        point.gameover()

    for brick in bricks:
        if(ball.distance(brick)<30):
            brick.kill()
            point.addpoint()


screen.exitonclick()