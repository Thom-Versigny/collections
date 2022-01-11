listone = [1,2,3,4,5,6,7,8,9,10]
listtwo = [2,4,6,8,10,12,14,16,18,20]

for x in range(10):
	plus= listone[x]+listtwo[x]
	print(f'{listone[x]} + {listtwo[x]} = {plus}')

for x in range(10):
	minus= listone[x]-listtwo[x]
	print(f'{listone[x]} - {listtwo[x]} = {minus}')

for x in range(10):
	keer= listone[x]*listtwo[x]
	print(f'{listone[x]} * {listtwo[x]} = {keer}')

for x in range(10):
	gedeeld= listone[x]/listtwo[x]
	print(f'{listone[x]} / {listtwo[x]} = {gedeeld}')