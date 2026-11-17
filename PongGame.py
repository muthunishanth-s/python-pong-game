import turtle
import tkinter
import winsound
import time

score_A_player = 0
score_B_player = 0

#display_screen
screen = turtle.Screen()
screen.setup(800, 600) # set with, height
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#leftPaddle
left_paddle = turtle.Turtle()  # create turtle Object
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.speed(0)
left_paddle.goto(-390,0)

#rightPaddle
right_paddle = turtle.Turtle()  # create turtle Object
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.speed(0)
right_paddle.goto(385,0)

#ball
ball = turtle.Turtle()  # create turtle object
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.dx = 0.13
ball.dy = 0.13

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 250)
pen.hideturtle()
pen.write(f"Player A: {score_A_player}   Player B: {score_B_player}", align="center", font=("Ariel",24,"normal"))

#moving paddles
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)

def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)

def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)

def right_paddle_down():
    right_paddle.sety(right_paddle.ycor()-20)

screen.listen()
screen.onkeypress(left_paddle_up, 'w')
screen.onkeypress(left_paddle_down, 's')
screen.onkeypress(right_paddle_up, 'Up')
screen.onkeypress(right_paddle_down, 'Down')


try:
    while True:
        screen.update()

        #ball movement
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)

        #not outOFBound of paddle
        if(right_paddle.ycor()+50 > 300):
            right_paddle.sety(250)
        if(right_paddle.ycor()-50 < -300):
            right_paddle.sety(-250)
        if(left_paddle.ycor()+50 > 300):
            left_paddle.sety(250)
        if(left_paddle.ycor()-50 < -300):
            left_paddle.sety(-250)
        

        #ball wall Collision
        if ball.ycor() > 299:
            ball.dy *= -1
        if ball.ycor() < -299:
            ball.dy *= -1
        #right wall
        if ball.xcor() > 399:
            ball.dx *= -1
            #update score
            score_A_player += 1
            pen.clear()
            pen.write(f"Player A: {score_A_player}   Player B: {score_B_player}", align="center", font=("Ariel",24,"normal"))

        #left wall
        if ball.xcor() < -399:
            ball.dx *= -1
            #update score
            score_B_player += 1
            pen.clear()
            pen.write(f"Player A: {score_A_player}   Player B: {score_B_player}", align="center", font=("Ariel",24,"normal"))

        #ball collision with paddle
        if (ball.xcor()>385) and (ball.ycor() < right_paddle.ycor()+50) and (ball.ycor() > right_paddle.ycor()-50):
            winsound.PlaySound("pong_game music.wav", winsound.SND_ASYNC)
            ball.dx *= -1
        if (ball.xcor()<-390) and (ball.ycor() < left_paddle.ycor()+50) and (ball.ycor() > left_paddle.ycor()-50):
            winsound.PlaySound("pong_game music.wav", winsound.SND_ASYNC)
            ball.dx *= -1

        if(score_A_player==5 or score_B_player==5):
            ball.clear()
            left_paddle.clear()
            right_paddle.clear()
            pen.clear()
            pen.write("GAME OVER", align="center", font=("Ariel",24,"normal"))
            time.sleep(1)


except tkinter.TclError:
    pass
