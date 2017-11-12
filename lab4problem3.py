class person(object):
	def __init__(self, name, age, city , gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender

	def eat(self,food):
		print("Yummy!!" + self.name + "is eating" + food)
	def hobby(self,game):
		print("yes!!" + self.name + "like to play" + game)

j = person("gilad" , "15 " , "Har Adar", "male")
j.eat("blincheses")
j.hobby("soccer")
