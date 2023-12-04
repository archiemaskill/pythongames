import unittest

from src.main import start_game


class GameTest(unittest.TestCase):
	@unittest.skip
	def test_smoke(self):
		start_game()
