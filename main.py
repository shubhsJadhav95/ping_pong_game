from turtle import Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)

# Create paddles and ball
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Keyboard controls
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Bounce on top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bounce on paddle hit
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_x()
        scoreboard.r_point()

    if (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        scoreboard.l_point()


    if ball.xcor() > 380:
        ball.reset_ball()


    if ball.xcor() < -380:
        ball.reset_ball()



screen.exitonclick()
