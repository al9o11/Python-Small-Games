import turtle
import winsound
window = turtle.Screen()
window.title("Clasic Pong by @al9o1")
window.bgcolor("black")
window.setup(width = 800, height=600)
window.tracer(0)

score_A = 0
score_B = 0

paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5,stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5,stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align = "center", font=("Courier",24,"normal"))


def paddle_A_Up():
    y = paddle_A.ycor()
    y+=20
    paddle_A.sety(y)
def paddle_A_Down():
    y = paddle_A.ycor()
    y-=20
    paddle_A.sety(y)
def paddle_B_Up():
    y = paddle_B.ycor()
    y+=20
    paddle_B.sety(y)
def paddle_B_Down():
    y = paddle_B.ycor()
    y-=20
    paddle_B.sety(y)

window.listen()
window.onkeypress(paddle_A_Up,"w")
window.onkeypress(paddle_A_Down,"s")
window.onkeypress(paddle_B_Up,"Up")
window.onkeypress(paddle_B_Down,"Down")

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1
        winsound.PlaySound("pong_wall_hit.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
        winsound.PlaySound("pong_wall_hit.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_A +=1
        pen.clear()
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        pen.write("Player A: {}  Player B: {}".format(score_A , score_B),align = "center", font=("Courier",24,"normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_B +=1
        pen.clear()
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
        pen.write("Player A: {}  Player B: {}".format(score_A , score_B),align = "center", font=("Courier",24,"normal"))

    if (ball.xcor()>340 and ball.xcor() <350) and (ball.ycor()< paddle_B.ycor() + 40 and ball.ycor()> paddle_B.ycor()):
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("paddle_hit.wav", winsound.SND_ASYNC)
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()< paddle_A.ycor() + 40 and ball.ycor()> paddle_A.ycor()):
        ball.setx(-340)
        ball.dx *=-1
        winsound.PlaySound("paddle_hit.wav", winsound.SND_ASYNC)