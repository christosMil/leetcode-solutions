class ParkingSystem:

	def __init__(self, big: int, medium: int, small: int):
		self.big = big
		self.medium = medium
		self.small = small
		self.my_dict = {1: self.big, 2: self.medium, 3: self.small}

	def addCar(self, carType: int) -> bool:
		if self.my_dict[carType] > 0:
			self.my_dict[carType] -= 1
			return True
		return False

obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))
