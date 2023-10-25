'''Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen
etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston
avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun.'''
import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='rootwadap',
    autocommit=True
    )

def get_airport_by_cordinates(user_input):
    cursor = connection.cursor()
    cursor.execute(f"select latitude_deg, longitude_deg FROM airport where ident = '{user_input}'")
    result = cursor.fetchall()
    return result




icao_code1 = input("Anna ensimmäisen lentokentän ICAO- koodi:")
airport1 = get_airport_by_cordinates(icao_code1)


icao_code2 = input("Anna ensimmäisen lentokentän ICAO- koodi:")
airport2 = get_airport_by_cordinates(icao_code2)

ans_distance = distance.great_circle(airport1,airport2)
print(f'Kahden kentän välinen etäisyys on {ans_distance}')






