'''Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin
JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava
GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
{"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.'''
'''Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
 lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna
  airport-taulun ident-sarakkeeseen.'''
import mysql.connector
from flask import Flask, request,Response
import json
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='rootwadap',
         autocommit=True
         )


palavelin = Flask(__name__)

@palavelin.route('/kenttä/<icao_code>')
def get_airport(icao_code):
    cursor = connection.cursor()
    cursor.execute(f"select name, municipality FROM airport where ident = '{icao_code}'")
    sql_result = cursor.fetchone()  # hakee ensimmäisen tulosrivin
    if sql_result:
        response_data = {"ICAO":icao_code,"name":sql_result[0],"municipality":sql_result[1]}
        status_code = 200
    else:
        response_data = {"msg":"ICAO not found"}
        status_code = 400
    response_data = json.dumps(response_data)
    response = Response(response=response_data,status=status_code,mimetype="application/json")
    return response


if __name__ =='__main__':
    palavelin.run(use_reloader=True,host='127.0.0.1',port=3000)
