import turtle as t

playerAscore = 0
playerBscore = 0

# create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("green")
window.setup(width=1000, height=700)
window.tracer(0)

# Creating the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-450, 0)

# Creating the right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(450, 0)

# Code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ballxdirection = 0.3
ballydirection = 0.3

bordedgeup= t.Turtle()
bordedgeup.speed(0)
bordedgeup.color("Blue")
bordedgeup.penup()
bordedgeup.hideturtle()
bordedgeup.goto(-450, 300)
bordedgeup.write("______________________________________________________________________________________________________________________________________________________")

bordedgedown= t.Turtle()
bordedgedown.speed(0)
bordedgedown.color("Blue")
bordedgedown.penup()
bordedgedown.hideturtle()
bordedgedown.goto(-450, -300)
bordedgedown.write("______________________________________________________________________________________________________________________________________________________")

# Code for creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Player A: {}     Player B: {} ".format(playerAscore, playerBscore),
                  align="center", font=('Monaco', 24, "normal"))


# code for moving the leftpaddle
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 40
    leftpaddle.sety(y)


def leftpaddledown():
    y = leftpaddle.ycor()
    y = y - 40
    leftpaddle.sety(y)


# code for moving the rightpaddle
def rightpaddleup():
    y = rightpaddle.ycor()
    y = y + 40
    rightpaddle.sety(y)



def rightpaddledown():
    y = rightpaddle.ycor()
    y = y - 40
    rightpaddle.sety(y)


# Assign keys to play
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # border set up
    if leftpaddle.ycor()>250:
        leftpaddle.goto(-450, 250)
    if leftpaddle.ycor()<-300:
        leftpaddle.goto(-450, -250)

    if rightpaddle.ycor()>270:
        rightpaddle.goto(450, 250)
    if rightpaddle.ycor()<-270:
        rightpaddle.goto(450, -250)


    if ball.ycor() > 300:
        ball.sety(300)
        ballydirection = ballydirection * -1
    if ball.ycor() < -300:
        ball.sety(-300)
        ballydirection = ballydirection * -1

    if ball.xcor() > 450:
        ball.goto(0, 0)
        rightpaddle.goto(450, 0)
        leftpaddle.goto(-450, 0)
        ballxdirection * -1
        playerAscore = playerAscore+ 1
        pen.clear()
        pen.write("Player A: {}     Player B: {} ".format(playerAscore, playerBscore),
                  align="center", font=('Monaco', 24, "normal"))


    if (ball.xcor()) < -450:  # Left width paddle Border
        ball.goto(0, 0)
        rightpaddle.goto(450, 0)
        leftpaddle.goto(-450, 0)
        ballxdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Player A: {}     Player B: {} ".format(playerAscore, playerBscore),
                  align="center", font=('Monaco', 24, "normal"))


    # Handling the collisions with paddles.

    if (ball.xcor() > 440) and (ball.xcor() < 450) and (
        ball.ycor() < rightpaddle.ycor() + 50 and ball.ycor() > rightpaddle.ycor() - 50):
        ball.setx(440)
        ballxdirection = ballxdirection * -1


    if (ball.xcor() < -440) and (ball.xcor() > -450) and (
            ball.ycor() < leftpaddle.ycor() + 50 and ball.ycor() > leftpaddle.ycor() - 50):
        ball.setx(-440)
        ballxdirection = ballxdirection * -1
