'''Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan
 tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi
 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä
 jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään
 käyttäjältä ohjelman suorituksen alussa.'''
import random
dice_maxnum = int(input('Anna arpakuution maksimi silmäluku:  '))
dicenum = 0
roll = 0
while dice_maxnum != dicenum:
    dicenum = random.randint(1,dice_maxnum)
    roll+=1
    print(f'Heitto {roll}: {dicenum}')

print(f'Sait nopan maksimi silmäluvun: {dice_maxnum}')






