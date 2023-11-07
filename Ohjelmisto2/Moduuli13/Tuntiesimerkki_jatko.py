from flask import Flask, request, Response, render_template
import json

app = Flask(__name__)
app.debug = True
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

    try:
        num = int(num)
    except ValueError:
        response_data = {
            "msg": "Input is not an integer",
            "input_num": num
        }
        status_code = 400
    else:

        if 0 < num < 100:
            result = num * num
            # response in dictinary format is translated to json automacically
            response_data = {
                "msg": "Calculation done",
                "input_num": num,
                "result": result
            }
            status_code = 200
        else:
            response_data = {
                "msg": "Input out of bounds",
                "input_num": num
            }
            status_code = 400

    # convert python dict to json format "manually"
    response_data = json.dumps(response_data)
    # setting up a status code for response needs Response object to be created
    response = Response(response=response_data, status=status_code, mimetype="application/json")
    return response

# https://flask.palletsprojects.com/en/2.3.x/errorhandling/

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    #jsonvast = json.dumps(vastaus)
    # return Response(response=jsonvast, status=404, mimetype="application/json")
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
