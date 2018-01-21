from turtle import *
import random
import math

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, radius, color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x, y)
		self.dx=dx
		self.dy=dy
		self.radius=radius
		self.shape("circle")
		self.shapesize(radius/10)
		self.color(color)
	def move(self , screen_width, screen_height):
		current_x=self.xcor()
		new_x=current_x+dx
		current_y=self.ycor()
		new_y=current_y+dy
		right_side_ball=new_x+radius
		left_side_ball=new_x-radius
		up_side_ball=new_y+radius
		bottom_side_ball=new_y-radius
		self.goto(new_x ,new_y)
		if right_side_ball>=screen_width or left_side_ball<= - screen_width:
			print("problem")
			self.dx=-self.dx
		if up_side_ball >= screen_height or bottom_side_ball <= -screen_height:
			print("problem")
			self.dy=-self.dy

