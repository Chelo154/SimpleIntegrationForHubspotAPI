from flask import Flask,jsonify
from routes import routes,oauth,deals


app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'response': 'This is the Simple Integration for Hubspot API by Marcelo de Jesús Núñez'})


app.register_blueprint(routes.blueprint)
app.register_blueprint(oauth.blueprint)
app.register_blueprint(deals.blueprint)

if __name__ == '__main__':
    app.run(host="localhost", port=8080)
