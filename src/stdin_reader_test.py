from src.stdin_reader import StdInReader


def test_non_configured_always_returns_1():
	reader = StdInReader.create_null()

	assert reader.read_line() == "1"
	assert reader.read_line() == "1"
	assert reader.read_line() == "1"

