from turtle import Turtle

class Ball(Turtle):
  def __init__ (self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()  
    # define the amount that the ball is going to move
    self.x_move = 10 
    self.y_move = 10
    self.move_speed = 0.1
     
  def move(self):
    # in order to move the ball, we have to add those mount to the X and Y coordinates
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  # when the ball needs to bounce off the top and bottom walls, we reverse the y cor by subtract instead of add.
  def bounce_y(self):
    self.y_move *= -1     

  # Incrase speed everytime the ball has been touched by the paddles
  def bounce_x(self):
    self.x_move *= -1
    self.move_speed *= 0.9 
    
  def reset_position(self):
    self.goto(0,0)
    self.bounce_x()
    
    
    
