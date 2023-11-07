'''Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa
aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa:
http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.'''
from flask import Flask
palavelin = Flask(__name__)
@palavelin.route('/alkuluku/<num>')
def get_root(num):
    num = int(num)
    if num % num == 0 and num % 1 == 0:
        prime = True
    else:
        prime = False
    response_data = {"Number": num, "isPrime": prime}
    return response_data


if __name__ =='__main__':
    palavelin.run(use_reloader=True,host='127.0.0.1',port=3000)

#esimerkki query http://127.0.0.1:3000/kukkuu?name=ville




if __name__ =='__main__':
    palavelin.run(use_reloader=True,host='127.0.0.1',port=3000)
