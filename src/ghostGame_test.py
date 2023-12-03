import unittest

from ghostGame import GhostGame
from src.stdout_printer import StdOutPrinter


class GameTest(unittest.TestCase):
	@staticmethod
	def test_prints_welcome_message():
		printer = StdOutPrinter.create_null()
		game = GhostGame(printer)
		tracker = printer.track_output()

		game.start()

		assert tracker.output() == [
			"Welcome to Ghost Game!",
			"There are 3 doors ahead, a ghost is behind one door",
			"You keep on choosing a door until it is a ghost door",
			"Each door without a ghost gets you 5 points",
			"Which door: 1, 2, or 3?"]

