#!flask/bin/python

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from resources import BrandListResource
from resources import BrandResource

api.add_resource(BrandListResource, '/brands', endpoint='brands')
api.add_resource(BrandResource, '/brands/<int:brand_id>', endpoint='brand')

if __name__ == '__main__':
    app.run(debug=True)
