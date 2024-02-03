from turtle import Screen, Turtle # import screen from turtle 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height= 600)
screen.tracer(0) # tracer stops the animation on turtle screen

#create pong paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

# get the screen to listen to keystrokes, so that the self can move up and down
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w") # the letters for keystrokes have to be lowercase
screen.onkey(l_paddle.go_down,"s")

 # the while loop manually update the screen and refrech it every single time. (because I use tracer method.)
game_is_on = True
while game_is_on:
  time.sleep(ball.move_speed) # ball speed
  screen.update()
  ball.move() # call a move method in Ball class
  
  #detect collision with wall
  if ball.ycor() > 280 or ball.ycor() <- 280:
    ball.bounce_y() #needs to bounce
    
    #detect collision with paddles
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() <- 320:
    ball.bounce_x() # collides with the r_paddle
    
  # detect when r_paddle misses
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()
    
  # detect when l_paddle misses
  if ball.xcor() < -380 :
    ball.reset_position()
    scoreboard.r_point()
# # this exitonclick method stops the screen from dissapearing until you click on the screen
screen.exitonclick()