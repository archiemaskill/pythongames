from output_tracking import OutputListener


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
		self.listener = OutputListener()

	def println(self, my_str):
		self.listener.emit(my_str)
		if self.is_nulled:
			pass
		else:
			print(my_str)

	def track_output(self):
		return self.listener.create_tracker()
