import pandas as pd
import ast
from flask import Flask, jsonify, request
from flask_restful import Api, reqparse, Resource

app = Flask(__name__)

imgData = {'data': str()}

@app.route('/receiveData', methods=['GET'])
def receiveData():
    # get image processed by CV algorithm and send back - just a float

    return

# android app needs to send back file in form of {'data': 'base64encodedstring'}
@app.route('/sendImage', methods=['PUT'])
def sendImage():
    imgData['data'] = request.json().to_dict()['data']
    return '', 200


if __name__ == '__main__':
    app.run()