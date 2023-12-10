from random import randint


class GhostDoor:

	@staticmethod
	def create():
		return GhostDoor(RealRandInt())

	@staticmethod
	def create_null(*door_nums):
		return GhostDoor(StubbedRandInt(door_nums))

	def __init__(self, rand_int):
		self.rand_int = rand_int

	def choose(self):
		return self.rand_int.get_rand()


class RealRandInt:
	@staticmethod
	def get_rand():
		return randint(1, 3)


class StubbedRandInt:

	def __init__(self, door_nums=()):
		self.configured_door_nums = door_nums
		self.current = 0

	def get_rand(self):
		if self.configured_door_nums:
			if self.current >= len(self.configured_door_nums):
				raise StopIteration("No more doors configured in nulled GhostDoor")
			else:
				item = self.configured_door_nums[self.current]
				if item < 1 or item > 3:
					raise ValueError("Value was: " + str(item))
				self.current += 1

				return item
		else:
			return 1
