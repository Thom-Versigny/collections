import random
def spelProgramma(spelList, minimum, maximum):
	rng=random.choice(range(minimum, maximum))
	for x in range(rng):
		print(random.choice(spelList))

spelProgramma(['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo'], 4, 100)