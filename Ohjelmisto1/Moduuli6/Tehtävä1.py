'''Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita
pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun
silmäluvun.'''
'''import random
def dice_roll():
    num = random.randint(1, 6)
    return num

flag = True

while flag == True:
    roll = dice_roll()
    if roll == 6:
        print(roll)
        flag = False
    else:
        print(roll)'''
import random

def dice_roll():
    dice_num = random.randint(1,6)
    print(f'{dice_num}')
    return dice_num
flag = True
input("Paina Enter:  ")
while flag:
    if dice_roll() == 6:
        (dice_roll)
        flag =  False
    else:
        dice_roll()


