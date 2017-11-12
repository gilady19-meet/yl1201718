class animal(object):
	def __init__(self, sound, name, age, favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy!!" + self.name + "is eating" + food)
	def descripition(self):
		print (self.name + "is" + self.age + "years old and love the color" + self.favorite_color)
	def make_sound(self):
		print (self.sound * 3)

j = animal("siii" , "cr7 " , "32", "white")
print(j.sound)
print(j.name)
print(j.age)
print(j.favorite_color)
j.eat("pizza")
j.descripition()
j.make_sound()
