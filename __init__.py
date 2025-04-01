from flask import Flask, render_template, jsonify
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
import requests
from collections import Counter

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.route('/tawarano/')
def meteo():
    # Données météo simulées
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

@app.route('/commits-data/')
def get_commit_minutes():
    url = 'https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits'  # Tu peux mettre l'URL de ton propre repo si tu veux
    response = requests.get(url)
    commits = response.json()

    minutes_list = []

    for commit in commits:
        try:
            date_str = commit['commit']['author']['date']
            date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
            minutes_list.append(date_obj.minute)
        except:
            continue

    count_by_minute = Counter(minutes_list)
    data = [{'minute': str(minute), 'count': count} for minute, count in sorted(count_by_minute.items())]

    return jsonify(results=data)

@app.route("/commits/")
def graphique_commits():
    return render_template("commits.html")

