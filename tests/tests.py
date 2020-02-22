import unittest

from encapsulation import Car
from abstraction import Library, Book
from inheritance_polymorphism import Animal, Cat, Dog, makeNoise

class TestCases(unittest.TestCase):
	def setUp(self):
		self.car = Car("red", "N93V7K")

		self.book1984 = Book("1984", "abcdef")
		self.bookTimeMachine = Book("1984", "abcdef")
		self.library = Library([ self.book1984, self.bookTimeMachine ])

		self.cat = Cat()
		self.dog = Dog()

	def test_car_getset_Color(self):
		self.assertEqual(self.car.getColor(), "red")
		self.car.setColor("blue")
		self.assertEqual(self.car.getColor(), "blue")

	def test_car_getLicensePlate(self):
		self.assertEqual(self.car.getLicensePlate(), "N93V7K")

	def test_library_findBookByTitle_existing(self):
		self.assertEqual(self.library.findBookByTitle("1984"), self.book1984)

	def test_library_findBookByTitle_nonexisting(self):
		self.assertEqual(self.library.findBookByTitle("not-existing"), None)

	def test_animal_eat(self):
		self.assertEqual(self.cat.eat(), "eating")

	def test_makeNoise_cat(self):
		self.assertEqual(makeNoise(self.cat), "meow")

	def test_makeNoise_dog(self):
		self.assertEqual(makeNoise(self.dog), "woof")
