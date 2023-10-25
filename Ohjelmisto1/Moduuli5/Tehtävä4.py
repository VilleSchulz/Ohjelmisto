'''Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien
 kysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain
 samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta
 niiden läpikäymiseen.'''

city_list= []
for i in range(5):
    print("Anna viiden kaupungin nimet")
    user_input = input(f'Anna kaupungin nimi nro. {i+1}: ')
    city_list.append(user_input)# lisää kaupungin listaan
print('Tässä viisi kaupunkia:')
for city in city_list: # tulostaa koko listan
    print(city)
