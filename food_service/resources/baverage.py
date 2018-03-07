from flask_restful import fields, marshal_with, reqparse, Resource
import random

def percentage(value):
    '''Return the value if it is a valid percentage. Else raise an exception.'''
    if value >= 0.0 and value <= 50.0:
        return value
    else:
        raise ValueError('{} is not a valid percentage'.format(value))

post_parser = reqparse.RequestParser()

post_parser.add_argument(
    'name', dest='name',
    type=str, required=True,
    help='The unique id of the baverage'
)

post_parser.add_argument(
    'alcohol_percentage', dest='alcohol_percentage',
    type=percentage, default=0.0,
    help='alcohol percentage of the baverage'
)

baverage_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'alcohol_percentage': fields.Float
}

def create_baverage(name, alcohol_percentage):
    return { 'id': random.randrange(1, 1500),
             'name': name,
             'alcohol_percentage': alcohol_percentage
    }

class Baverage(Resource):

    def get(self, id):
        return {'id': id,
                'name': 'coffee',
                'alcohol_percentage': 0.0
        }

    # marshal is pythons' internal serialization
    @marshal_with(baverage_fields)
    def post(self):
        args = post_parser.parse_args() # cleaned
        baverage = create_baverage(args.name, args.alcohol_percentage)
        return baverage
