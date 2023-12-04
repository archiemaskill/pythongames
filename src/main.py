from src.ghost_game import GhostGame
from src.stdout_printer import StdOutPrinter


def start_game():
	GhostGame(StdOutPrinter.create()).run()


if __name__ == '__main__':
	start_game()
