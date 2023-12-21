'''
Created on 

@author: Deepak raj

source:
    https://stackoverflow.com/questions/41492721/in-python-flask-how-do-you-get-the-path-parameters-outside-of-the-route-functio
    https://www.linkedin.com/pulse/topics/engineering-s166/artificial-intelligence-(ai)-s2407/
'''

from flask import Flask, render_template, Request, redirect, url_for
import jsonify
import json

app = Flask(__name__)

DATA_FILENAME = 'data.json'

# Read JSON data from a file
with open(DATA_FILENAME, 'r') as file:
    json_data = json.load(file)

@app.route('/')
def page_index():
    return render_template('index.html', data = json_data)


if __name__ == '__main__':
    app.run(
        host    = '0.0.0.0',
        port    = 5004,
        debug   = True
    )