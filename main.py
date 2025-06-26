import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

UP = "Up"
DOWN = "Down"
W_KEY = "w"
S_KEY = "s"
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)
scoreboard = Scoreboard()
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
screen.listen()
screen.onkey(fun= right_paddle.go_up, key=UP)
screen.onkey(fun= right_paddle.go_down, key=DOWN)
screen.onkey(fun= left_paddle.go_up, key=W_KEY)
screen.onkey(fun= left_paddle.go_down, key=S_KEY)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision to  wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.left_point()

    #Detect left paddle miss
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.right_point()





screen.exitonclick()