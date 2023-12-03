from random import randint


class GhostDoor:

	@staticmethod
	def create():
		return GhostDoor(False)

	@staticmethod
	def create_null(*door_nums):
		return GhostDoor(True, door_nums)

	def __init__(self, is_nulled, door_nums=()):
		self.is_nulled = is_nulled
		self.door_nums = door_nums
		self.current = 0

	def choose(self):
		if self.is_nulled:
			if self.door_nums:
				if self.current >= len(self.door_nums):
					raise StopIteration("No more doors configured in nulled GhostDoor")
				else:
					item = self.door_nums[self.current]
					if item < 1 or item > 3:
						raise ValueError("Value was: " + str(item))
					self.current += 1

					return item
			else:
				return 1
		else:
			return randint(1, 3)
