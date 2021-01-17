from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
api = Api(app)

db_url = 'mysql://root:''@217.0.0.1/movie'
db = SQLAlchemy(app)

helloworld_post_args = reqparse.RequestParser()
helloworld_post_args.add_argument("name", type=str)
helloworld_post_args.add_argument("age", type=int)
helloworld_post_args.add_argument("city", type=str)


class HelloWorld(Resource):
    def get(self, name):
        d = db.select("category")
        return {"data": d}
    def post(self, name):
        return helloworld_post_args.parse_args()

api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
