from turtle import *
import random
import math

class Rectangle(Turtle):
	def __init__(self, x , y , hight , width , color):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.hight = hight
		self.width = width
		self.color(color)
		