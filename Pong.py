# Simple Pong Game in Python

import turtle

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_left = turtle.Turtle()
paddle_left.speed(0)    # 0 for maximum possible speed
paddle_left.shape("square")
paddle_left.color("blue")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()     #Sets the current pen state to PENUP. Turtle will move around the screen, but will not draw when its pen state is PENUP
paddle_left.goto(-350, 0)

# Paddle B
paddle_right = turtle.Turtle()
paddle_right.speed(0)    # 0 for maximum possible speed
paddle_right.shape("square")
paddle_right.color("blue")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(50)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 # every time the ball moves, it moves by 2 pixels
ball.dy = 0.2

# Function to move the paddle
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)

# Keyboard binding to listen for keyboard input
wn.listen()
wn.onkeypress(paddle_left_up, "w")
wn.onkeypress(paddle_left_down, "s")
wn.onkeypress(paddle_right_up, "Up")
wn.onkeypress(paddle_right_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
       ball.setx(340)
       ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
       ball.setx(-340)
       ball.dx *= -1