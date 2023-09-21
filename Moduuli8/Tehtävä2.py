'''Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
 lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
  lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.'''


import mysql.connector


connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='rootwadap',
         autocommit=True
         )

def get_airport_by_type(iso_country):
    cursor = connection.cursor()
    cursor.execute(f"select type, count(*) FROM airport where iso_country = '{iso_country}' group by type")
    result = cursor.fetchall()  # hakee ensimmäisen tulosrivin
    if result:
        return result
    else:
       return "No results"


user_input = input("Anna lentokentän Maa koodi: ")

for type in  get_airport_by_type(user_input): #tulostaa rivikerrallaan tuplena eli monikkona
    print(f'[{type[0]}]: {type[1]} kpl')