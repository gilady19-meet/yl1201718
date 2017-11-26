from turtle import *
import random
colormode(255)
red=random.randint(0 ,255)
blue=random.randint(0 ,255)
green=random.randint(0 ,255)




# class Square(Turtle):
# 	def __init__(self, size):
# 		Turtle.__init__(self)
# 		self.shapesize(size)
# 		self.shape("square")
# 		self.size = size
# 		self.color(red, green, blue)
# 	def random_color(self):
# 		print(red, green, blue)

class Rectangle(Turtle):
	def __init__(self, width , height):
		Turtle.__init__(self)
		register_shape("new" , ((0,0) , (0, width) , (height , width) , (height , 0)))		
		self.shape("new")
		self.setheading(90)

class Square(Rectangle):
	def __init__(self, ectangle):
		Square.__init__(self)

		

Rectangle1=Rectangle(100 , 50)
 

mainloop()