from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import  Score
import time

screen=Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.textinput(title="instructions",prompt="Welcome to Pong. Use W and S keys to move the left paddle up and down and the "
                                             "up and down arrow keys to move the right paddle.")

r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
score=Score()

screen.listen()
screen.onkeypress(r_paddle.move_up,key="Up")
screen.onkeypress(r_paddle.move_down,key="Down")

screen.onkeypress(l_paddle.move_up,key="w")
screen.onkeypress(l_paddle.move_down,key="s")
game_is_on=True

while game_is_on:
    screen.update()
    ball.move_ball()
    time.sleep(ball.move_speed)

    #detect collision w/ wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision w/ r_paddle
    if ball.xcor()>320 and ball.distance(r_paddle)<50:
        ball.setx(320)
        ball.bounce_x()

    if ball.xcor()<-320 and ball.distance(l_paddle)<50:
        ball.setx(-320)
        ball.bounce_x()


    #detect when paddle misses the ball
    if ball.xcor()>380:
        score.l_point()
        ball.reset_position()

    if ball.xcor()<-380:
        score.r_point()
        ball.reset_position()


screen.exitonclick()