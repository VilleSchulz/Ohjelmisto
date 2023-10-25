import mysql.connector
"""
# Alla SQL-komennot uuden tietokantakohtaisen (flight_game) käyttäjätunnuksen luomiseksi.
# Korvaa 'username' ja 'password' omilla sanoilla, HUOM! älä laita mitään
# henkilökohtaisessa käytössäsi olevia tunnuksia!
CREATE USER IF NOT EXISTS 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON `flight_game`.* TO 'username'@'localhost';
"""

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='rootwadap',
         autocommit=True
         )

'''cursor = connection.cursor()
#cursor.execute("select iso_country, name FROM country where iso_country = 'FI'")
#result = cursor.fetchone()# hakee ensimmäisen tulosrivin
cursor.execute("select iso_country, name, continent FROM country")

result = cursor.fetchall()
print(result)

print(cursor.rowcount)
for country in  result: #tulostaa rivikerrallaan tuplena eli monikkona
    print(f'Maa: {country[0]}, koodi: {country[1]}')
'''

def get_country_by_iso_code(iso_code):
    cursor = connection.cursor()
    cursor.execute(f"select iso_country, name FROM country where iso_country = '{iso_code}'")
    result = cursor.fetchone()  # hakee ensimmäisen tulosrivin
    if result:
        return result[1]
    else:
       return "No results"




def update_country_by_iso_code(iso_code, country_name):#Päivitetään maiden nimiä kannassa
    cursor = connection.cursor()
    sql= cursor.execute(f"UPDATE country SET name='{country_name}' where iso_country='{iso_code}'")
    cursor.execute(sql)
    if cursor.rowcount > 0:
        return f'koodi {iso_code} päivitetty, uusi maan nimi: {country_name}'
    else:
        f'koodia {iso_code} ei löytynyt, muutoksia ei tehty.'

while True:
    country = get_country_by_iso_code(input("Annakoodi: "))
    print(country)
    #country = get_country_by_iso_code("FI")
    #print(country)

    country_code = input("Anna muokattava koodi: ")
    new_name =  input("Anna maalle uusi nimi: ")
    update_country_by_iso_code(country_code,new_name)