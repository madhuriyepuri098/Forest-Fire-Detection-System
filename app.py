from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/detect", methods=["POST"])
def detect():
    return jsonify({
        "result": "FIRE DETECTED!",
        "fire_area": "2.12%"
    })
@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js")

@app.route("/style.css")
def style():
    return send_from_directory(".", "style.css")

