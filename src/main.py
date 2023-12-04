from game_state import GameState
from ghost_door import GhostDoor
from ghost_game import GhostGame
from stdin_reader import StdInReader
from stdout_printer import StdOutPrinter


def start_game():
	GhostGame(
		StdOutPrinter.create(),
		GhostDoor.create(),
		StdInReader.create(),
		GameState.new()).run()


if __name__ == '__main__':
	start_game()
