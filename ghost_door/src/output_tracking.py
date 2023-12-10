class OutputListener:
	def __init__(self):
		self.trackers = []

	def create_tracker(self):
		tracker = OutputTracker(self)
		self.trackers.append(tracker)
		return tracker

	def emit(self, data):
		for tracker in self.trackers:
			tracker.add(data)

	def remove(self, tracker):
		self.trackers.remove(tracker)


class OutputTracker:
	def __init__(self, listener):
		self._output = []
		self.listener = listener

	def add(self, data):
		self._output.append(data)

	def output(self):
		return self._output

	def clear(self):
		self._output.clear()

	def stop(self):
		self.listener.remove(self)
