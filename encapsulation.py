class Car:
	def __init__(self, color, licensePlate):
		"""
		Note that Python does not have truly private variables.
		The convention is to prefix private variables with '__'
		"""
		self.__color = color
		self.__licensePlate = licensePlate

	def getColor(self):
		return self.__color

	def setColor(self, color):
		self.__color = color

	def getLicensePlate(self):
		return self.__licensePlate
