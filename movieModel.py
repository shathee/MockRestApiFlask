from main import db

db.metadata.clear()

class MovieModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    adult = db.Column(db.String(5), nullable=True)
    budget = db.Column(db.Numeric)
    genres = db.Column(db.String(50))
    homepage = db.Column(db.String(50))
    original_language = db.Column(db.String(3))
    production_companies = db.Column(db.String(50))
    release_date = db.Column(db.String(12))
    revenue = db.Column(db.Numeric)
    rating = db.Column(db.Numeric)



    # def __repr__(self):
    #     return f"Movies(id={id}, name={name})"

db.create_all()