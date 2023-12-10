#!/usr/bin/env python
from game_state import GameState
from ghost_door import GhostDoor
from ghost_game import GhostGame
from stdin_reader import StdInReader
from stdout_printer import StdOutPrinter


if __name__ == '__main__':
	game = GhostGame(
		GameState.new(),
		GhostDoor.create(),
		StdInReader.create(),
		StdOutPrinter.create())

	game.run()
