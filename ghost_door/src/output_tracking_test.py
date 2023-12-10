from .output_tracking import OutputListener, OutputTracker


# listener tests
def test_can_create_output_tracker():
	listener = OutputListener()
	tracker = listener.create_tracker()
	assert tracker is not None
	assert isinstance(tracker, OutputTracker)


def test_trackers_are_updated_with_emits():
	listener = OutputListener()
	tracker1 = listener.create_tracker()
	listener.emit("first data")

	tracker2 = listener.create_tracker()
	listener.emit("second data")

	listener.remove(tracker1)
	listener.emit("third data")

	assert tracker1.output() == ["first data", "second data"]
	assert tracker2.output() == ["second data", "third data"]


# tracker tests
def test_add_data_to_trackers():
	tracker = OutputTracker(OutputListener())

	tracker.add("some data")
	tracker.add("some more data")

	output = tracker.output()
	assert output == ["some data", "some more data"]

	tracker.clear()
	assert tracker.output() == []


def test_stopping_tracker_removes_its_listener():
	listener = OutputListener()
	tracker = listener.create_tracker()

	listener.emit("first data")
	assert tracker.output() == ["first data"]

	tracker.stop()
	listener.emit("second data")
	assert tracker.output() == ["first data"]

