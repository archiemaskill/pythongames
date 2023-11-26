class StdOutPrinter:
	@staticmethod
	def create():
		instance = StdOutPrinter(False)
		return instance

	@staticmethod
	def create_null():
		instance = StdOutPrinter(True)
		return instance

	def __init__(self, is_nulled):
		# Define attributes
		self.is_nulled = is_nulled

	def println(self, my_str):
		if self.is_nulled:
			pass
		else:
			print(my_str)
