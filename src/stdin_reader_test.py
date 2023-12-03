import unittest

from src.stdin_reader import StdInReader


def test_non_configured_always_returns_1():
	reader = StdInReader.create_null()

	assert reader.read_line() == "1"
	assert reader.read_line() == "1"
	assert reader.read_line() == "1"


def test_can_be_configured():
	reader = StdInReader.create_null("1", "2", "3")

	assert reader.read_line() == "1"
	assert reader.read_line() == "2"
	assert reader.read_line() == "3"


class MyTestClass(unittest.TestCase):
	def test_raises_exception_when_runs_out_of_configured_values(self):
		reader = StdInReader.create_null("1")
		reader.read_line()

		# act
		with self.assertRaises(StopIteration) as context:
			reader.read_line()

		# assert
		self.assertEqual(str(context.exception), "No more lines configured in nulled StdInReader")
