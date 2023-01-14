from flask import Flask
from flask_restful import Api, reqparse, Resource

app = Flask(__name__)
api = Api(app)

class test(Resource):
    def get(self):
        data = 1
        return {'data': data}, 200

api.add_resource(test, '/test')

if __name__ == '__main__':
    app.run()