from flask import Flask, jsonify
import requests
import tg


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "API is working fine"


@app.route("/<query>")
def telegram_(query):
    return jsonify(tg.telegram(query))


if __name__ == "__main__":
    #app.debug = True
    app.run(host="0.0.0.0",port= 5000)