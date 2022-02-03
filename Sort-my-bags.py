import random

def mnmadd(hoeveel):
    mnmDictionaryBag = {
    }
    mmkleur = ['geel','rood','oranje','blauw','groen','bruin']
    zakMM = []
    for x in range(hoeveel):
        mnmDictionaryBag[random.choice(mmkleur)] = 0
    for x in range(hoeveel):
        mnmDictionaryBag[random.choice(list(mnmDictionaryBag))] += 1
        zakMM.append(random.choice(mmkleur))
    print(('geel', zakMM.count('geel')))
    print(('rood', zakMM.count('rood')))
    print(('oranje', zakMM.count('oranje')))
    print(('blauw', zakMM.count('blauw')))
    print(('groen', zakMM.count('groen')))
    print(('bruin', zakMM.count('bruin')))
    print(mnmDictionaryBag)


hoeveel=int(input('hoeveel kleuren (M&Ms) wilt u toevoegen aan de zak: '))
mnmadd(hoeveel)

