'''Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.'''

import random
dicecount = int(input('Anna arpakuutioiden lukumäärä: '))
dicenum_result = []
for i in range(dicecount):
    dicenum = random.randint(1,6)
    print(f'{i+1}.Luku:  {dicenum}')
    dicenum_result.append(dicenum)
print(f'Silmälukujen summa on: {sum(dicenum_result)}')

