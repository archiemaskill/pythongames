from src.ghost_door import GhostDoor
from src.stdin_reader import StdInReader
from stdout_printer import StdOutPrinter


class GhostGame:
	def __init__(self, printer, ghost_door, stdin_reader):
		self.printer = printer
		self.ghost_door = ghost_door
		self.stdin_reader = stdin_reader

	def start(self):
		self.printer.println("Welcome to Ghost Game!")
		self.printer.println("There are 3 doors ahead, a ghost is behind one door")
		self.printer.println("You keep on choosing a door until it is a ghost door")
		self.printer.println("Each door without a ghost gets you 5 points")
		self.printer.println("Which door: 1, 2, or 3?")

		ghostDoor = self.ghost_door.choose()
		userGuess = self.stdin_reader.read_line()

		if ghostDoor == int(userGuess):
			self.printer.println("GHOST! GHOST!! GHOST!!!")


def start_game():
	GhostGame(StdOutPrinter.create()).start()


if __name__ == '__main__':
	start_game()
