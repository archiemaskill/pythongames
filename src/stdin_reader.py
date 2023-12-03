class StdInReader:

	def __init__(self, lines):
		self.lines = lines
		self.current = 0
		pass

	@staticmethod
	def create_null(*lines):
		instance = StdInReader(lines)
		return instance

	def read_line(self):
		if self.lines:
			item = self.lines[self.current]
			self.current += 1
			return item
		else:
			return "1"
