# Ghost Door

Run Ghost Door using one of the following commands:

    * python main.py
    * ./main.py

# Program Design

Ghost Door is a very simple game that is essentially a random number generator, and an input prompt.
The player has to avoid guessing the random number for as long as possible.

This game can easily be implemented in a single production file containing 20-30 lines of code.

This implementation, however, is much larger - about 150 lines spread over 6 files.
Why is this?

Smaller implementations tend to be structured in a way that is highly untestable.
This implementation was developed using test-driven development (TDD) and is highly testable.
The extra size is due to the boilerplate required for splitting up the game's responsibilities
into separate classes.  Additionally, I chose to use James Shore's Nullables Testing Pattern, where
embedded stubs for testing are included in the production code. While many would immediately perceive
this as a problem, I have found that in reality it is not, and that the advantages it brings to testing
are substantial.


`ghost_door` is the class that randomly generates a number between 1 and 3.  It's a 'nullable' class meaning that, when
created in a null state, it can be told which numbers to generate.  The nulled state also has a reasonable default,
where it just generates an infinite series of "1"s.

`stdout_printer` is the class responsible for writing lines of text to stdout.  It is nullable, and when created in a
nulled state it does not write anything to stdout, preventing noise in the test output.  It also uses `output_tracking`,
so that tests can check what exactly was being printed.

`stdin_reader` is the class responsible for reading lines of user input.  Again, it's nullable and when created in a
nulled state, it either assumes a reasonable default (user entering an infinite series of "1"s) or can be configured
to be provided with the user's input.

`ghost_game` ties everything together, it's the main game loop and accepts all the collaborative objects in its constructor.

`main.py` - this is the file that kicks everything off.  As is typical for the entry point of non-trivial programs, it is
not easily testable. This is because it is essentially a laundry list of production collaborators, passed into the main
game object. To unit-test this would require overriding the stdin and stdout (messy!) and the unpredictability of the
random number generator would also create non-trivial challenges.
