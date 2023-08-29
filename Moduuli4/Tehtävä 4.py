'''Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.'''
import random
numrndm = random.randint(1, 10)
guess = 0
while guess != numrndm:
    guess = int(input('Arvaa numero: '))
    if guess < numrndm:
        print("Arvaamasi numero on liian pieni!")
    if guess > numrndm:
        print("Arvaamasi numero on liian suuri!")
else:
    print('Arvasit oikein!')




