from turtle import *
import random
import math

turtle.register_shape("shoot.gif")
class Shoot(Turtle):
	def __init__(self, x, y, dx, dy, radius, color , speed , size , demage, shape):
		Turtle.__init__(self)
		self.pu()
		self.goto(x, y)
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.radius=radius
		self.speed=speed
		self.size=size
		self.demage=demage
		self.shape("shoot.gif")
	def move(self , screen_width, screen_height):
		current_x=self.xcor()
		new_x=current_x+self.dx
		current_y=self.ycor()
		new_y=current_y+self.dy
		right_side_ball=new_x+self.radius
		left_side_ball=new_x-self.radius
		up_side_ball=new_y+self.radius
		bottom_side_ball=new_y-self.radius
		self.goto(new_x ,new_y)
