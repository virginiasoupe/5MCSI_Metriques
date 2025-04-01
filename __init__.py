from flask import Flask, render_template, jsonify
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.route('/tawarano/')
def meteo():
    # 🔧 Données simulées (car l'API d'origine est obsolète)
    results = [
        {'Jour': 1711900000, 'temp': 14.3},
        {'Jour': 1711986400, 'temp': 16.7},
        {'Jour': 1712072800, 'temp': 15.1},
        {'Jour': 1712159200, 'temp': 18.4},
    ]
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def monhistogramme():
    return render_template("histogramme.html")
