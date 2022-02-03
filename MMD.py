import random

def mnmadd(hoeveel):
  mnmDictionaryBag = {
  }
  mmkleur = ["geel","rood",'oranje','blauw','groen',"bruin"]
  for x in range(hoeveel):
    mnmDictionaryBag[random.choice(mmkleur)] = 0
  for x in range(hoeveel):
    mnmDictionaryBag[random.choice(list(mnmDictionaryBag))] += 1
  return mnmDictionaryBag
  
hoeveel=int(input('hoeveel kleuren (M&Ms) wilt u toevoegen aan de zak: '))
mnmDictionaryBag=mnmadd(hoeveel)
print(mnmDictionaryBag)