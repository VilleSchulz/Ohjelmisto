'''Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.'''

import random
dicecount = int(input('Anna arpakuutioiden lukumäärä: '))
dicenum_result = []
for _ in range(dicecount):
    dicenum = random.randint(1,6)
    dicenum_result.append(dicenum)

print(f'Silmälukujen summa on: {sum(dicenum_result)}')

