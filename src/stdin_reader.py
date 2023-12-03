class StdInReader:

	@staticmethod
	def create():
		instance = StdInReader("", False)
		return instance

	@staticmethod
	def create_null(*lines):
		instance = StdInReader(lines, True)
		return instance

	def __init__(self, lines, is_nulled):
		self.lines = lines
		self.current = 0
		self.is_nulled = is_nulled
		pass

	def read_line(self):
		if self.is_nulled:
			return self.stubbed_input()
		else:
			return self.real_input()

	@staticmethod
	def real_input():
		return input()

	def stubbed_input(self):
		if self.lines:
			if self.current >= len(self.lines):
				raise StopIteration("No more lines configured in nulled StdInReader")
			item = self.lines[self.current]
			self.current += 1
			return item
		else:
			return "1"
