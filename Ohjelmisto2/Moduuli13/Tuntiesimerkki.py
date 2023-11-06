from flask import Flask, request, Response
import json

palavelin = Flask(__name__)
@palavelin.route('/')
def get_root():
    return "Moro"

#esimerkki query http://127.0.0.1:3000/kukkuu?name=ville
@palavelin.route('/kukkuu')
def get_kukkuu():
    #print(request.args)
    name = request.args.get("name")
    return f"haista paska {name}"

#esimerkki query http://127.0.0.1:3000/kukkuu/ville
@palavelin.route('/kukkuu/<name>')
def get_kukkuu2(name):
    #print(request.args)

    return f"haista paska {name}"
#esimerkki query http://127.0.0.1:3000/kukkuu/ville
@palavelin.route('/kukkuu/<name>/<age>')
def get_kukkuu3(name,age):
    #print(request.args)

    return f"haista paska {name}, {age}v"

#esimerkki query http://127.0.0.1:3000/multiply/25
#esimerkki response '{num:5, result: 25}'
@palavelin.route('/multiply/<num>')
def multiply(num):
    # To Do: refactor code: create response

    try:
        num = int(num)
    except ValueError:
        response_data = {"msg": "input is not integer", "input_num": num}
        # convert python dict to json format "manually"
        # response_data = json.dumps(response_data)
        response = Response(response=response_data, status=400, mimetype="application/json")
        return response

    if 0< num < 100:
        result = num * num
        response_data = {"msg":"Calculation done","input_num": num , "result": result}
        return response_data
    else:
        response_data = {"msg": "input out of bounds", "input_num": num}
        #convert python dict to json format "manually"
        #response_data = json.dumps(response_data)
        response = Response(response= response_data, status=400,mimetype="application/json")
        return response


if __name__ =='__main__':
    palavelin.run(use_reloader=True,host='127.0.0.1',port=3000)



