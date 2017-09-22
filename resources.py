
from models import Brand
from db import session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

brand_fields = {
    'id': fields.Integer('brand_id'),
    'name': fields.String,
    'website': fields.String(default=''),
    'uri': fields.Url('brands', absolute=True),
}

model_fields = { 
    'id': fields.Integer('model_id'),
    'brand_id': fields.Integer('brand_id'),
    'name': fields.String(absolute=True),
    'year': fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='Name should be a string', required=True)
parser.add_argument('website', type=str, help='Website should be a string')

class BrandResource(Resource):
    @marshal_with(brand_fields)
    def get(self, brand_id):
        brand = session.query(Brand).filter(Brand.id == brand_id).first()
        if not brand:
            abort(404, message="Brand {} doesn't exist".format(id))
        return brand

    def delete(self, brand_id):
        brand = session.query(Brand).filter(Brand.id == brand_id).first()
        if not brand:
            abort(404, message="Brand {} doesn't exist".format(id))
        session.delete(brand)
        session.commit()
        return {}, 204

    @marshal_with(brand_fields)
    def put(self, brand_id):
        parsed_args = parser.parse_args()
        brand = session.query(Brand).filter(Brand.id == brand_id).first()
        brand.name = parsed_args['name']
        brand.website = parsed_args['website']
        session.add(brand)
        session.commit()
        return brand, 201


class BrandListResource(Resource):
    @marshal_with(brand_fields)
    def get(self):
        brands = session.query(Brand).all()
        return brands

    @marshal_with(brand_fields)
    def post(self):
        parsed_args = parser.parse_args()
        brand = Brand()
        brand.name = parsed_args['name']
        brand.website = parsed_args['website']
        session.add(brand)
        session.commit()
        return brand, 201
