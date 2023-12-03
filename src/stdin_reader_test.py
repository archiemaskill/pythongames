import unittest
from io import StringIO

from stdin_reader import StdInReader
from unittest.mock import patch


class Reader(unittest.TestCase):

	@patch("sys.stdin", StringIO("first line\nsecond line\n\n"))
	def test_reads_user_input_from_stdin(self):
		reader = StdInReader.create()

		self.assertEqual(reader.read_line(), "first line")
		self.assertEqual(reader.read_line(), "second line")
		self.assertEqual(reader.read_line(), "")


class NulledReader(unittest.TestCase):

	def test_non_configured_always_returns_the_default_value(self):
		reader = StdInReader.create_null()

		self.assertEqual(reader.read_line(), "1")
		self.assertEqual(reader.read_line(), "1")
		self.assertEqual(reader.read_line(), "1")

	def test_can_be_configured(self):
		reader = StdInReader.create_null("1", "2", "3")

		self.assertEqual(reader.read_line(), "1")
		self.assertEqual(reader.read_line(), "2")
		self.assertEqual(reader.read_line(), "3")

	def test_raises_exception_when_runs_out_of_configured_values(self):
		reader = StdInReader.create_null("1")
		reader.read_line()

		# act
		with self.assertRaises(StopIteration) as context:
			reader.read_line()

		# assert
		self.assertEqual(str(context.exception), "No more lines configured in nulled StdInReader")
