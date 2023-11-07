from flask import Flask, request, Response
import json

app = Flask(__name__)
# print(__name__)

@app.route('/')
def get_root():
    return "Moro maailma!"

# Example query: http://127.0.0.1:3000/kukkuu?name=Matti&age=25
@app.route('/kukkuu')
def get_kukkuu():
    # print(request.args)
    name = request.args.get("name")
    age = request.args.get("age")
    return f"No kukkuu vaan, {name}, {age} vuotta!"

# Example query: http://127.0.0.1:3000/kukkuu/Matti/25
@app.route('/kukkuu/<name>/<age>')
def get_kukkuu_v2(name, age):
    return f"No kukkuu vaan, {name}, {age} vuotta!"

# Example query: http://127.0.0.1:3000/multiply/5
# Example response in json: '{input_num: 5, result: 25}'
# input Num must be between 0-100
@app.route('/multiply/<num>')
def multiply(num):
    # TODO: refactor code: create response object and return it only once
    try:
        num = int(num)
    except ValueError:
        response_data = {"msg": "Input is not an integer", "input_num": num}
        # convert python dict to json format "manually"
        response_data = json.dumps(response_data)
        # setting up a status code for response needs Response object to be created
        response = Response(response=response_data, status=400, mimetype="application/json")
        return response
    if 0 < num < 100:
        result = num * num
        # response in dictinary format is translated to json automacically
        response_data = {"msg": "Calculation done", "input_num": num, "result": result}
        return response_data
    else:
        response_data = {"msg": "Input out of bounds", "input_num": num}
        # convert python dict to json format "manually"
        response_data = json.dumps(response_data)
        # setting up a status code for response needs Response object to be created
        response = Response(response=response_data, status=400, mimetype="application/json")
        return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
