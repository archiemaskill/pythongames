class GhostDoor:
	@staticmethod
	def create_null(*door_nums):
		return GhostDoor(door_nums)

	def __init__(self, door_nums):
		self.door_nums = door_nums
		self.current = 0

	def choose(self):
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
