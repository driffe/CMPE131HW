from myapp import db

class City(db.Model):
    name = db.Column(db.String(64), unique=True, index=True)
    rank = db.Column(db.Integer, primary_key=True)
