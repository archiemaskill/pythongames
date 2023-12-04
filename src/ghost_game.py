class GhostGame:
	def __init__(self, game_state, ghost_door, stdin_reader, stdout_writer):
		self.writer = stdout_writer
		self.ghost_door = ghost_door
		self.reader = stdin_reader
		self.game_state = game_state
		self.score = 0

	def run(self):
		if not self.game_state.is_game_started:
			self.welcome_player()

		while True:
			self.writer.println("Which door: 1, 2, or 3?")
			ghost_door = self.ghost_door.choose()
			user_guess = self.reader.read_line()

			if ghost_door == int(user_guess):
				self.writer.println("GHOST! GHOST!! GHOST!!!")
				break
			else:
				self.writer.println("You earned 5 points :)")
				self.score += 5

		self.writer.println("Your score = " + str(self.score))

	def welcome_player(self):
		self.writer.println("Welcome to Ghost Game!")
		self.writer.println("There are 3 doors ahead, a ghost is behind one door")
		self.writer.println("You keep on choosing a door until it is a ghost door")
		self.writer.println("Each door without a ghost gets you 5 points")
