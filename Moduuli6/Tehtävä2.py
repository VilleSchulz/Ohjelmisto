'''Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan
 tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi
 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä
 jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään
 käyttäjältä ohjelman suorituksen alussa.'''
'''
import random
dice_maxnum = int(input('Anna arpakuution maksimi silmäluku:  '))
dicenum = 0
roll = 0
while dice_maxnum != dicenum:
    dicenum = random.randint(1,dice_maxnum)
    roll+=1
    print(f'Heitto {roll}: {dicenum}')

print(f'Sait nopan maksimi silmäluvun: {dice_maxnum}')'''

import random
roll = 0
def dice_roll(i):
    dice_num = random.randint(1,dice_num_amount)
    print(f'Heitto: {i} Numero {dice_num}')
    return dice_num
flag = True
dice_num_amount = int(input("Anna nopan tahkojen määrä: "))
throw = 0
i = 1
while flag:
    if dice_roll(i) == dice_num_amount:
        flag =  False

    else:

        dice_roll(i)
        i += 1








