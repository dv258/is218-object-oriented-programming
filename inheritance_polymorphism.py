class Animal:
	def __init__(self):
		pass

	def eat(self):
		return "eating"

	def sleep(self):
		return "sleeping"

	def noise(self):
		return None

class Cat(Animal):
	def __init__(self):
		pass

	def noise(self):
		return "meow"

class Dog(Animal):
	def __init__(self):
		pass

	def noise(self):
		return "woof"

def makeNoise(animal):
	return animal.noise()
