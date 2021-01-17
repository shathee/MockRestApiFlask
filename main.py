from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db_url = 'mysql://root:''@127.0.0.1/movie'
db = SQLAlchemy(app)

class MovieModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    adult = db.Column(db.String(5), nullable=True)
    budget = db.Column(db.Numeric)
    genres = db.Column(db.String(50))
    homepage = db.Column(db.String(50))
    original_language = db.Column(db.String(3))
    production_companies = db.Column(db.String(50))
    release_date = db.Column(db.String)
    revenue = db.Column(db.Numeric)
    rating = db.Column(db.Numeric)



# db.create_all()

helloworld_post_args = reqparse.RequestParser()
helloworld_post_args.add_argument("name", type=str)
helloworld_post_args.add_argument("age", type=int)
helloworld_post_args.add_argument("city", type=str)


movie_post_args = reqparse.RequestParser()
movie_post_args.add_argument("name", type=str)



class HelloWorld(Resource):
    def get(self, name):
        return {"data": name}
    def post(self, name):
        return helloworld_post_args.parse_args()

resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'adult' : fields.String,
    'budget' : fields.Float,
    'genres' : fields.String,
    'homepage' : fields.String,
    'original_language' : fields.String,
    'production_companies' : fields.String,
    'release_date' : fields.String,
    'revenue' : fields.Float,
    'rating' : fields.Float
}

class Movies(Resource):
    @marshal_with(resource_fields)
    def get(self):
        # result = MovieModel.query.with_entities(MovieModel.adult).all()
        result = MovieModel.query.limit(50).all()
        
        return result
        
    @marshal_with(resource_fields)    
    def post(self):
        args = movie_post_args.parse_args()
        m = MovieModel(name=args['name'])
        db.session.add(m)
        db.session.commit()
        return m, 201 
    

class Movie(Resource):
    @marshal_with(resource_fields)
    def get(self, id):
        result = MovieModel.query.filter_by(id=id).first()
        return result
    
    def post(self):
        return movie_post_args.parse_args()

api.add_resource(HelloWorld, "/helloworld/<string:name>")
api.add_resource(Movies, "/movies/")
api.add_resource(Movie, "/movies/<int:id>")



if __name__ == "__main__":
    app.run(debug=True)
