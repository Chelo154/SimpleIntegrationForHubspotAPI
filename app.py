from flask import Flask,Response,jsonify
from routes import routes
from domain.Entity import Entity
from serializers.entity import  EntityJsonEncoder
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'response': 'This is the Simple Integration for Hubspot API by Marcelo de Jesús Núñez'})


app.register_blueprint(routes.blueprint)

if __name__ == '__main__':
    app.run(port=8080)
