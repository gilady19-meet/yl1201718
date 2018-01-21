from turtle import *
import random
import math

class Rectangle(Turtle):
	def __init__(self, x , y , hight , width , color):
		Turtle.__init__(self)
		self.goto(x, y)
		self.hight = hight
		self.width = width
		self.color(color)
		self.shape("square")
		self.shapesize(width/20 , hight/20)

	def top(self):
		return self.ycor()+0.5*self.hight
	def right(self):
		return self.xcor()+0.5*self.width
	def bottom(self):
		return self.ycor()-0.5*self.hight
	def left(self):
		return self.xcor()-0.5*self.width


a = Rectangle(100 , 300, 10, 4, "blue") 
b = Rectangle(2 , 4, 12, 17, "red") 



if (a.top()> b.bottom() and a.right()>b.left() and a.bottom()<b.top() and a.left()<b.right()):
	print(True)
else:
	print(False)

mainloop()