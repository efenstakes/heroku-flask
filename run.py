from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def home():
    return { 'page': 'home', 'status': 'running' }

@app.route('/about')
def about():
    return { 'page': 'about', 'status': 'abouting' }



if __name__ == '__main__':
    app.run( debug=True )
