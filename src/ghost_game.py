class GhostGame:
	def __init__(self, printer, ghost_door, stdin_reader, game_state):
		self.printer = printer
		self.ghost_door = ghost_door
		self.stdin_reader = stdin_reader
		self.game_state = game_state
		self.score = 0

	def run(self):
		if not self.game_state.is_game_started:
			self.welcome_player()

		while True:
			self.printer.println("Which door: 1, 2, or 3?")
			ghost_door = self.ghost_door.choose()
			user_guess = self.stdin_reader.read_line()

			if ghost_door == int(user_guess):
				self.printer.println("GHOST! GHOST!! GHOST!!!")
				break
			else:
				self.printer.println("You earned 5 points :)")
				self.score += 5

		self.printer.println("Your score = " + str(self.score))

	def welcome_player(self):
		self.printer.println("Welcome to Ghost Game!")
		self.printer.println("There are 3 doors ahead, a ghost is behind one door")
		self.printer.println("You keep on choosing a door until it is a ghost door")
		self.printer.println("Each door without a ghost gets you 5 points")
