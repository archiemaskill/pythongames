import os
import random

monsters = ["SKELETON", "GHOST", "HEADLESS AXEMAN"]
floor = 0
Rdollar = ""
S = -1
GF = -1
P = -1
RM = -1

my_globals = {

}


def clear_console():
	os.system('clear' if os.name == 'posix' else 'cls')


def subroutine400():
	global S, GF, P, Rdollar
	if GF == 1:
		P = P + S * 2
		Rdollar = "AAAHHHH!"


def subroutine420():
	global S, GF
	index = random.randint(0, 2)
	monster_name = monsters[index]
	S = random.randint(0, 4) + floor + index * 2
	print("\nAhead you see a " + monster_name)
	GF = 1


def get_user_input():
	the_input = None
	while the_input != "G" and the_input != "R":
		the_input = input()
	return the_input


def go_sub520():
	global P, RM
	Rdollar = "YOU FELL THROUGH A TRAP DOOR!"
	RM = RM - 5
	P = P + 10


def restart_game():
	raise ValueError("Can't restart game - not yet implemented")


def run_game():
	global Rdollar, floor, GF, P, RM
	Rdollar = "Good luck"
	RM = 0
	my_globals["H"] = 9
	# generate 10 to 19, inclusive
	my_globals["M"] = random.randint(10, 19)
	P = 50

	while True:
		clear_console()
		print("\n\n")
		print("Tower of Terror")
		print("===============")
		print("\n" + str(Rdollar))

		Rdollar = ""
		floor = int(RM / 5)
		R = RM - floor * 5 + 1

		print("\nYou are on")
		if floor == 0:
			print("the ground floor")
		if floor == 6:
			print("the top floor")
		if 0 < floor < 6:
			print("floor " + str(floor))
		print("in room " + str(R))
		print("\nThe time is " + str(my_globals["H"]) + "." + str(my_globals["M"]) + " PM")
		print("\nYour pulse rate is " + str(P))
		GF = 0
		if RM == 30:
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
			RM = RM - 1
			P = P - 5
		if RM == -1:
			RM = 0
		my_globals["M"] = my_globals["M"] + random.randint(1, 3)
		if my_globals["M"] > 59:
			my_globals["M"] = my_globals["M"] - 60
			my_globals["H"] = my_globals["H"] + 1
		if my_globals["H"] == 12:
			print("\nIt's midnight!")
			print("\nToo late!")
			raise ValueError("Ending game")
		if P > 150:
			print("\nYou have gone mad and")
			print("\nLeapt from a window")
			raise ValueError("Ending game")
		if P < 40:
			P = 40
		if floor == TR and random.random() > 0.5:
			go_sub520()


if __name__ == '__main__':
	run_game()
