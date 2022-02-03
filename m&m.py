import random
mmkleur = ['oranje','blauw','groen','bruin']
def randomMenM(MMaantal):
	zakMM=[]
	for x in range(MMaantal):
		zakMM.append(random.choice(mmkleur))
	return zakMM

MMaantal=int(input('hoeveel kleuren (M&Ms) wilt u toevoegen aan de zak: '))
zakMM = randomMenM(MMaantal)
print(zakMM)