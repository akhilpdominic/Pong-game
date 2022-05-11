import turtle
import os
import time

wn=turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()


pen.goto(0,0)
pen.write("PING-PONG",align="center",font=("Courier",50,"normal"))
Player_A=wn.textinput("NIM","Name of Player A:")
Player_B=wn.textinput("NIM","Name of Player B:")
time.sleep(1)
pen.clear()
pen.write("READY....",align="center",font=("Courier",50,"normal"))
time.sleep(3)

pen.clear()
#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5

#score
score_a=0
score_b=0



pen.goto(0,260)
pen.write("{}:  {} {}:  {}".format(Player_A,score_a,Player_B,score_b),align="center",font=("Courier",24, "normal"))


def paddle_a_up():
    y=paddle_a.ycor()
    y=y+20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#Binding the functions on keyboard
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


while True:
    wn.update()
    #move ball

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if(ball.ycor()>290):
        ball.sety(290)
        ball.dy*=-1
        os.system("afplay bounce.m4a&")

    if(ball.ycor()<-290):
        ball.sety(-290)
        ball.dy*=-1
        os.system("afplay bounce.m4a&")

    if(ball.xcor()>390):
        ball.setx(0)
        ball.sety(0)
        score_a+=1
        pen.clear()
        pen.write("{}:  {} {}:  {}".format(Player_A,score_a,Player_B,score_b),align="center",font=("Courier",24, "normal"))
        ball.dx*=-1

    if(ball.xcor()<-390):
        ball.setx(0)
        ball.sety(0)
        score_b+=1
        pen.clear()
        pen.write("{}:  {} {}:  {}".format(Player_A,score_a,Player_B,score_b),align="center",font=("Courier",24, "normal"))
        ball.dx*=-1
        

    if(ball.xcor()>340 and ball.xcor()<350 and ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
        os.system("afplay bounce.m4a&")
        ball.dx*=-1
        

    if(ball.xcor()<-340 and ball.xcor()>-350 and ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        os.system("afplay bounce.m4a&")
        ball.dx*=-1

        