'''minun_lista = [1, 2, 3, 4, 5, 6]
print(minun_lista)
minun_monikko = (1, 2, 3 ,4 ,5 ,6)
minun_monikko2 = 2, 3, 4, 5, 6 ,7
print(minun_monikko2)
minun_string = '123456'
'''
#litan sisältöa voi muokata
minun_lista= [0]
print(minun_lista)
minun_set = {"monopoli", "Shakki", "Jalkapallo"}
print(minun_set)

minun_set.add('Juoksu')
print(minun_set)
'''
#monikon ja string sisältöa ei voi muokata


#koodiesimerkki materiaalista


viikonpäivät = ('maanantai','tiistai','keskiviikko','torstai','perjantai','lauantai','sunnuntai')

järjestynumero = int(input("Anna viikonpäivän järjestysnumero: "))
viikonpäivä =  viikonpäivät[järjestynumero - 1]

print(f'{järjestynumero}. viikonpäivä on {viikonpäivä}')

hedelmät = ('Appelsiini', 'Banaani', 'Omena')
(eka, toka, kolmas) = hedelmät
print (f'Hedelmiä ovat {eka}, {toka}, {kolmas}')'''

# Sanakirjat
oppilaat = {'Aapeli': 25, 'Bertta': 45, 'Cecilia': 16, 'Daniel': 45, 'Emma': 34}

#printataan koko sanakirja
#avaimet
for i in oppilaat:
    print(i)
# arvot
for i in oppilaat:
    print(oppilaat[i])


#mitä ovat tietueet / items
print(oppilaat.items())
#mitkä ovat avaimia sanakirjassa?
print(oppilaat.keys())
#mitkä ovat arvoja sanakirjassa?
print(oppilaat.values())

print(oppilaat['Daniel'])
#lisätään mikäli frederikkii ei löydy
oppilaat['Frederikki']= 100
print(oppilaat.items())

#muokataan ikää,
oppilaat['Aapeli']= 76
print(oppilaat.items())
#Voit etsiä onko avain sanakirjassa IN:llä
nimi = input("Anna nimi: ")
if nimi in oppilaat:
    print (f"Henkilön {nimi} puhelinnumero on {oppilaat[nimi]}.")

#poista tietue
del oppilaat['Aapeli']
print(oppilaat.items())

#toinen tapa poistaa, tallenna Aapelin tiedot muuttujaan
aapelin_ikä = oppilaat.pop('Daniel')
print(f'Daniel poistettiin mutta ikä jäi talteen: {Danielin_ikä}')


