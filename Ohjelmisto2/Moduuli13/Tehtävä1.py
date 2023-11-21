'''Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa
aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa:
http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.'''
import json

from flask import Flask,Response
palavelin = Flask(__name__)
@palavelin.route('/alkuluku/<num>')
def get_root(num):
    try:
        num = int(num)
    except ValueError:
        response_data = {"msg":"Input is not integer",
                         "input_num": num
                         }
        status_code = 400
    else:
        if num % num == 0 and num % 1 == 0:
            prime = True
        else:
            prime = False
        response_data = {"Number": num, "isPrime": prime}
        status_code = 200
    response_data = json.dumps(response_data)
    response = Response(response=response_data, status=status_code, mimetype= "application/json")
    return response


if __name__ =='__main__':
    palavelin.run(use_reloader=True,host='127.0.0.1',port=3000)







