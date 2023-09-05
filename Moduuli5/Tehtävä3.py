'''Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.'''
isPrime = True
num = int(input("Anna luku: "))

for i in range(2, num):
    if num % i ==0:
        isPrime = False
    #print('Numero ei ole alkuluku')

print("Alkulukutesti suoritettu")
if isPrime == True:
    print(f'luku {num} on alkuluku')
else:
    print('Ei ole alkuluku')