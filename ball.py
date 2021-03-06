from turtle import *
import random
import math

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, radius, color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x, y)
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.radius=radius
		self.shape("circle")
		self.shapesize(radius/10)
		self.color(color)
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
		if right_side_ball>=screen_width or left_side_ball<= - screen_width:
			print("problem")
			self.dx=-self.dx
		if up_side_ball >= screen_height or bottom_side_ball <= -screen_height:
			print("problem")
			self.dy=-self.dy

	def __str__(self):
		return "" + str(self.radius) +"\t"+ str(self.color()) +"\t"+ str(self.xcor()) +"\t"+ str(self.ycor()) +"\t"+ str(self.dx) +"\t"+ str(self.dy) 
