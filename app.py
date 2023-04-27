import os
import json
from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
import time


import logging

#from init import initvars
from Morph.stopwords import TextProcessor
from Morph.textproc import text_processing


app = Flask(__name__)
CORS(app)

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/init', methods=['GET'])
def init():
    global tp
    tp = TextProcessor() # class for removing stopwords from text
    return 'Init complete!'


init()

# rename columns
if __name__ == '__main__':
    app.run()
    app.config['DEBUG'] = True


@app.route('/textproc', methods=['POST'])
def textproc():
        print("textproc function")
        request_data = request.get_json()
        text = request_data["text"]
        criteria = request_data["criteria"]
        print(f'{text} {criteria}')
        result = text_processing(text, criteria)
        print (result)
        result = jsonify(result)
        print (result)
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Access-Control-Allow-Origin'] = '*'
        return result, 200, headers



