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
	if (ball1.shapesize()[0]*10+ball2.shapesize()[0]*10) >= Distance(ball1.xcor() , ball2.xcor() , ball1.ycor() , ball2.ycor()) :
		print("the balls are colide")
	else:
		print("NO COLIDE")


ball2.goto(100 , 100)
check_collision(ball1 , ball2)
ball2.goto(50, 50)
check_collision(ball1 , ball2)
ball2.goto(0, 150)
check_collision(ball1 , ball2)


balls = [ball1,ball2]

for i in balls:
	if (balls[0].shapesize()[0]*10+balls[1].shapesize()[0]*10) >= Distance(balls[0].xcor() , balls[1].xcor() , balls[0].ycor() , balls[1].ycor()) :
		print("colide")



mainloop()