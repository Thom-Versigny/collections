listone = [1,2,3,4,5,6,7,8,9,10]
listtwo = [2,4,6,8,10,12,14,16,18,20]

def addAndDisplayLists (listone, listtwo):
	for x in range(10):
		plus= listone[x]+listtwo[x]
		print(f'{listone[x]} + {listtwo[x]} = {plus}')

def substractAndDisplayLists (listone, listtwo):
	for x in range(10):
		minus= listone[x]-listtwo[x]
		print(f'{listone[x]} - {listtwo[x]} = {minus}')

def multiplyAndDisplayLists (listone, listtwo):
	for x in range(10):
		keer= listone[x]*listtwo[x]
		print(f'{listone[x]} * {listtwo[x]} = {keer}')

def divideAndDisplayLists (listone, listtwo):
	for x in range(10):
		gedeeld= listone[x]/listtwo[x]
		print(f'{listone[x]} / {listtwo[x]} = {gedeeld}')

addAndDisplayLists (listone, listtwo)
print('------------')
substractAndDisplayLists (listone, listtwo)
print('------------')
multiplyAndDisplayLists (listone, listtwo)
print('------------')
divideAndDisplayLists (listone, listtwo)