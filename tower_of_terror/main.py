import os
import random

monsters = ["SKELETON", "GHOST", "HEADLESS AXEMAN"]
floor = 0

my_globals = {
	"S": -1,
	"GF": -1
}


def clear_console():
	os.system('clear' if os.name == 'posix' else 'cls')


def subroutine400():
	if my_globals["GF"] == 1:
		my_globals["P"] = my_globals["P"] + my_globals["S"] * 2
		my_globals["R"] = "AAAHHHH!"


def subroutine420():
	index = random.randint(0, 2)
	monster_name = monsters[index]
	my_globals["S"] = random.randint(0, 4) + floor + index * 2
	print("\nAhead you see a " + monster_name)
	my_globals["GF"] = 1


def get_user_input():
	the_input = None
	while the_input != "G" and the_input != "R":
		the_input = input()
	return the_input


def go_sub520():
	my_globals["R"] = "YOU FELL THROUGH A TRAP DOOR!"
	my_globals["RM"] = my_globals["RM"] - 5
	my_globals["P"] = my_globals["P"] + 10


def restart_game():
	raise ValueError("Can't restart game - not yet implemented")


if __name__ == '__main__':
	my_globals["R"] = "Good luck"
	my_globals["RM"] = 0
	my_globals["H"] = 9
	# generate 10 to 19, inclusive
	my_globals["M"] = random.randint(10, 19)
	my_globals["P"] = 50

	while True:
		clear_console()
		print("\n\n")
		print("Tower of Terror")
		print("===============")
		print("\n" + str(my_globals["R"]))

		my_globals["R"] = ""
		floor = int(my_globals.get("RM") / 5)
		my_globals["R"] = my_globals["RM"] - floor * 5 + 1

		print("\nYou are on")
		if floor == 0:
			print("the ground floor")
		if floor == 6:
			print("the top floor")
		if 0 < floor < 6:
			print("floor " + str(floor))
		print("in room " + str(my_globals.get("R")))
		print("\nThe time is " + str(my_globals["H"]) + "." + str(my_globals["M"]) + " PM")
		print("\nYour pulse rate is " + str(my_globals["P"]))
		my_globals["GF"] = 0
		if my_globals["RM"] == 30:
			print("Well done")
			raise ValueError("Ending game")
		TR = random.randint(1, 9)
		if random.random() > 0.6:
			subroutine420()
		print("\nRetreat or go on (R/G)")
		my_input = get_user_input()
		if my_input == "G":
			subroutine400()
		if my_input == "R":
			my_globals["RM"] = my_globals["RM"] - 1
			my_globals["P"] = my_globals["P"] - 5
		if my_globals["RM"] == -1:
			my_globals["RM"] = 0
		my_globals["M"] = my_globals["M"] + random.randint(1, 3)
		if my_globals["M"] > 59:
			my_globals["M"] = my_globals["M"] - 60
			my_globals["H"] = my_globals["H"] + 1
		if my_globals["H"] == 12:
			print("\nIt's midnight!")
			print("\nToo late!")
			raise ValueError("Ending game")
		if my_globals["P"] > 150:
			print("\nYou have gone mad and")
			print("\nLeapt from a window")
			raise ValueError("Ending game")
		if my_globals["P"] < 40:
			my_globals["P"] = 40
		if floor == TR and random.random() > 0.5:
			go_sub520()
