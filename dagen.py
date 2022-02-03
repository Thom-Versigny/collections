dagen = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']

print('Alle dagen van de week zijn:')
for x in range(7):
    print(dagen[x])
print('De werkdagen zijn:')
for x in range(5):
    print(dagen[x])
print('De weekenddagen zijn:')
for x in [5, 6]:
    print(dagen[x])
print('Alle dagen van de week in omgekeerde volgorde zijn:')
for x in range(6, -1, -1):
    print(dagen[x])
print('De werkdagen in omgekeerde volgorde zijn: ')
for x in range(4, -1, -1):
    print(dagen[x])
print('De weekenddagen in omgekeerde volgorde zijn:')
for x in range(6, 4, -1):
    print(dagen[x])
