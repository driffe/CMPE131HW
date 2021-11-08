from myapp import db

class City(db.Model):
    city_name = db.Column(db.String(64), unique=True, index=True)
    city_rank = db.Column(db.Integer, primary_key=True)
    city_visited = db.Column(db.Boolean)

    def __repr__(self):
        return '<City {}>' .format(self.city_name)
    
    def __init__(self, city_name, city_rank, city_visited):
        self.city_name = city_name
        self.city_rank = city_rank
        self.city_visited = city_visited

