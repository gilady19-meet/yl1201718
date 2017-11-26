from turtle import *
import random
colormode(255)
red=random.randint(0 ,255)
blue=random.randint(0 ,255)
green=random.randint(0 ,255)

class Hexagon(Turtle):
	def __init__(self, size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.begin_poly()
		self.color(red, green, blue)
		self.begin_fill()
		for i in range(6):
			self.forward(size)
			self.left(60)
		self.end_poly()
		self.end_fill()
		register_shape('Hexagon' , self.get_poly())
		self.shape("Hexagon")

a=Hexagon(100) 
print(a)

mainloop()