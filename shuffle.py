import random

secure_random = random.SystemRandom()
suits = ["c", "d", "h", "s"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

F1 = secure_random.choice(ranks) + random.choice(suits)
F2 = secure_random.choice(ranks) + random.choice(suits)
F3 = secure_random.choice(ranks) + random.choice(suits)
turn = secure_random.choice(ranks) + random.choice(suits)
river = secure_random.choice(ranks) + random.choice(suits)

Flop = F1 + " " + F2 + " " + F3

def shuffle():
	F1 = secure_random.choice(ranks) + random.choice(suits)
	F2 = secure_random.choice(ranks) + random.choice(suits)
	F3 = secure_random.choice(ranks) + random.choice(suits)
	turn = secure_random.choice(ranks) + random.choice(suits)
	river = secure_random.choice(ranks) + random.choice(suits)

	Flop = F1 + " " + F2 + " " + F3
	
	print("Flop:")
	print(Flop+'\n')
	print("Turn:")
	print(turn+'\n')
	print("River:")
	print(river+'\n')
	print("Showdown:")
	print(Flop + " " + turn + " " + river + '\n')

	retry_prompt()

def retry_prompt():
	choice = input("Wanna shuffle again? [Y/N]?")

	if choice == "Y":
		shuffle()

	elif choice == "N":
		exit()
	else:
		print("\n" + "Error, invalid input")
		retry_prompt()

shuffle();
