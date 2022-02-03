import random
spelList=['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']
def spelProgramma(spelList, minimum, maximum):
	rng=random.choice(range(minimum, maximum))
	for x in range(rng):
		print(random.choice(spelList))

spelProgramma(spelList, 2, 7)