import unittest

from ghostGame import GhostGame, start_game
from src.ghost_door import GhostDoor
from src.stdin_reader import StdInReader
from src.stdout_printer import StdOutPrinter


class GameTest(unittest.TestCase):

	def test_prints_welcome_message(self):
		printer = StdOutPrinter.create_null()
		game = GhostGame(printer, GhostDoor.create_null(), StdInReader.create_null())
		tracker = printer.track_output()

		game.start()

		self.assertListEqual(tracker.output()[:5], [
			"Welcome to Ghost Game!",
			"There are 3 doors ahead, a ghost is behind one door",
			"You keep on choosing a door until it is a ghost door",
			"Each door without a ghost gets you 5 points",
			"Which door: 1, 2, or 3?"])

	def test_player_chooses_the_ghost_door(self):
		printer = StdOutPrinter.create_null()
		tracker = printer.track_output()
		game = GhostGame(printer, GhostDoor.create_null(2), StdInReader.create_null("2"))

		game.start()

		self.assertListEqual(tracker.output()[:6], [
			"Welcome to Ghost Game!",
			"There are 3 doors ahead, a ghost is behind one door",
			"You keep on choosing a door until it is a ghost door",
			"Each door without a ghost gets you 5 points",
			"Which door: 1, 2, or 3?",
			"GHOST! GHOST!! GHOST!!!"])

	@unittest.skip
	def test_smoke(self):
		start_game()
