import unittest

from game_state import GameState
from ghost_door import GhostDoor
from ghost_game import GhostGame
from stdin_reader import StdInReader
from stdout_printer import StdOutPrinter


class GameTest(unittest.TestCase):

	def test_welcomes_player_when_starting_new_game(self):
		printer = StdOutPrinter.create_null()
		tracker = printer.track_output()
		game = GhostGame(GameState.new(), GhostDoor.create_null(), StdInReader.create_null(), printer)

		game.run()

		tracker_output = tracker.output()
		self.assertTrue(self.starts_with([
			"Welcome to Ghost Game!",
			"There are 3 doors ahead, a ghost is behind one door",
			"You keep on choosing a door until it is a ghost door",
			"Each door without a ghost gets you 5 points"], tracker_output))

	def test_player_chooses_the_ghost_door(self):
		printer = StdOutPrinter.create_null()
		game = GhostGame(GameState.running(), GhostDoor.create_null(2), StdInReader.create_null("2"), printer)
		tracker = printer.track_output()

		game.run()

		tracker_output = tracker.output()
		self.assertListEqual(tracker_output, [
			"Which door: 1, 2, or 3?",
			"GHOST! GHOST!! GHOST!!!",
			"Your score = 0"])

	def test_player_plays_several_rounds(self):
		printer = StdOutPrinter.create_null()
		game = GhostGame(
			GameState.running(),
			GhostDoor.create_null(1, 2, 3),
			StdInReader.create_null("2", "1", "3"),
			printer)
		tracker = printer.track_output()

		game.run()

		tracker_output = tracker.output()
		self.assertListEqual(tracker_output, [
			"Which door: 1, 2, or 3?",
			"You earned 5 points :)",
			"Which door: 1, 2, or 3?",
			"You earned 5 points :)",
			"Which door: 1, 2, or 3?",
			"GHOST! GHOST!! GHOST!!!",
			"Your score = 10"])

	@staticmethod
	def starts_with(sublist, big_list):
		return big_list[:len(sublist)] == sublist
