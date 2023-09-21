'''Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
 lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna
  airport-taulun ident-sarakkeeseen.'''
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='rootwadap',
         autocommit=True
         )

def get_airport_by_icao_code(icao_code):
    cursor = connection.cursor()
    cursor.execute(f"select name, municipality FROM airport where ident = '{icao_code}'")
    result = cursor.fetchone()  # hakee ensimmäisen tulosrivin
    if result:
        return result
    else:
       return "No results"


user_input = input("Anna lentokentän ICAO-koodi: ")
print(get_airport_by_icao_code(user_input))