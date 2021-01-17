from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
# db_url = 'mysql://root:''@127.0.0.1/movie'
db = SQLAlchemy(app)

class MovieModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    # def __repr__(self):
    #     return f"Movies(id={id}, name={name})"

db.create_all()

helloworld_post_args = reqparse.RequestParser()
helloworld_post_args.add_argument("name", type=str)
helloworld_post_args.add_argument("age", type=int)
helloworld_post_args.add_argument("city", type=str)


class HelloWorld(Resource):
    def get(self, name):
        return {"data": name}
    def post(self, name):
        return helloworld_post_args.parse_args()

resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String
}

class Movie(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        result = MovieModel.query.filter_by(id=id).first()
        return result
    def post(self):
        return id

api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(Movie, "/movies/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)
