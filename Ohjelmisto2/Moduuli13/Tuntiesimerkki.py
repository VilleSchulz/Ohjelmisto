from flask import Flask

palavelin = Flask(__name__)
@palavelin.route('/')
def get_root():
    return "Moro"

palavelin.run()
