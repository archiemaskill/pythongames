import sys
from stdout_printer import StdOutPrinter
from io import StringIO
import pytest


@pytest.fixture
def setup_and_teardown(self):
	yield
	sys.stdout = sys.__stdout__


def test_non_nulled_prints_to_stdout():
	sut = StdOutPrinter.create()
	captured_stdout = StringIO()
	sys.stdout = captured_stdout

	sut.println('Here is some output')

	assert captured_stdout.getvalue() == "Here is some output\n"


def test_nulled_does_not_print_to_stdout():
	sut = StdOutPrinter.create_null()
	captured_stdout = StringIO()
	sys.stdout = captured_stdout

	sut.println('Here is some output')

	assert captured_stdout.getvalue() == ""
