from turtle import *
import random
import math

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)
		self.radius=radius

ball1 = Ball(15 , "blue", 10) 
ball2 = Ball(5 , "red", 20) 

def Distance(x1, x2, y1, y2):
	d = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	return d

	


def check_collision(ball1 , ball2):
	if ball1.radius+ball2.radius > Distance(ball1.xcor() , ball2.xcor() , ball1.ycor() , ball2.ycor()) :
		print("the balls are colide")


check_collision(ball1 , ball2)






mainloop()