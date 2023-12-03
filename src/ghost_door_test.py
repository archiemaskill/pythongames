import unittest

from src.ghost_door import GhostDoor


class NulledGhostDoor(unittest.TestCase):
	def test_non_configured_always_returns_default(self):
		ghost_door = GhostDoor.create_null()

		self.assertEqual(ghost_door.choose(), 1)
		self.assertEqual(ghost_door.choose(), 1)
		self.assertEqual(ghost_door.choose(), 1)

	def test_configured_returns_given_values(self):
		ghost_door = GhostDoor.create_null(3, 1, 2)

		self.assertEqual(ghost_door.choose(), 3)
		self.assertEqual(ghost_door.choose(), 1)
		self.assertEqual(ghost_door.choose(), 2)

	def test_raises_exception_when_runs_out_of_configured_values(self):
		ghost_door = GhostDoor.create_null(3, 1)
		ghost_door.choose()
		ghost_door.choose()

		# act
		with self.assertRaises(StopIteration) as context:
			ghost_door.choose()

		# assert
		self.assertEqual(str(context.exception), "No more doors configured in nulled GhostDoor")

