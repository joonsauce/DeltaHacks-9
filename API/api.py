import requests
from convert import *
from flask import Flask, jsonify, request

app = Flask(__name__)

imgData = {'data': str()}

@app.route('/receiveData', methods=['GET'])
def receiveData(x, y):
    data = {'datax': x, 'datay': y}
    return jsonify(data), 200

# android app needs to send back file in form of {'data': 'base64encodedstring'}
@app.route('/sendImage', methods=['PUT'])
def sendImage():
    imgData['data'] = request.json['data']
    convert(imgData['data'])
    return '', 200


if __name__ == '__main__':
    app.run()