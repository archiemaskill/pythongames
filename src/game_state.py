class GameState:
	@staticmethod
	def new():
		return GameState(False)

	@staticmethod
	def running():
		return GameState(True)

	def __init__(self, is_game_started):
		self.is_game_started = is_game_started

	def is_game_started(self):
		return self.is_game_started()
