#!flask/bin/python

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from resources import BrandListResource
from resources import BrandResource

api.add_resource(BrandResource, '/brands', endpoint='brands')
api.add_resource(ModelResource, '/models', endpoint='models')
api.add_resource(GeometryResource, '/geometry', endpoint='geometry')

if __name__ == '__main__':
    app.run(debug=True)
