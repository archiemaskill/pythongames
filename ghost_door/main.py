#!/usr/bin/env python
from src.game_state import GameState
from src.ghost_door import GhostDoor
from src.ghost_game import GhostGame
from src.stdin_reader import StdInReader
from src.stdout_printer import StdOutPrinter


if __name__ == '__main__':
	game = GhostGame(
		GameState.new(),
		GhostDoor.create(),
		StdInReader.create(),
		StdOutPrinter.create())

	game.run()
