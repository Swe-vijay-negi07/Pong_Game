#Step 1 : Create Screen
#Step 2 : Create and move a paddle
#Step 3 : Create another paddle
#Step 4 : Create the ball and make it move
#Step 5 : Detects collision with wall and bounce
#Step 6 : Detect collision with paddle
#Step 7 : Detect when paddle
#Step 8 : Keep Score



from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

#=========== Section 1 - Creating screen=======
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height = 600)
screen.title("Pong")
screen.tracer(0)
#================creating the dot line between two player--============
line=Line() #object of line



#============Section 2 and 3 - Creating the paddle  and moving it====================
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

# =========== Section 4 - Creating the ball object and move it (moving part  is in while loop)================
ball = Ball()#object of class Ball

#=================Section 8 - Creating the object=====
scoreboard = Scoreboard() #object of the class Scoreboard.



screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")



game_is_on = True
while game_is_on:
    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move() #section 4 part only....


    #============ Section 5 - detect collision with wall and bounce===========
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #=========== Section 6 - detect collision with paddle=============
    
    #detect collision with r_paddle and l_paddle
    if ball.distance (r_paddle)<55 and ball.xcor()>320 or ball.distance(l_paddle)<55 and ball.xcor()<-320:
        ball.bounce_x()


#=============================Section 7 ===================
        
    #=============Detect R paddle misses==================
    if ball.xcor() > 380:     
        ball.reset_position() 
        scoreboard.l_point()  
    #=============Detect L paddle misses===================
    if ball.xcor() < -380:   
        ball.reset_position()
        scoreboard.r_point()  
        
        
    
screen.exitonclick()
