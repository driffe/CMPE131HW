from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TopCities(FlaskForm):
    city_name = StringField('City Name', validators=[DataRequired()])
    city_rank = IntegerField('City Rank', validators=[DataRequired()])
    city_visited = BooleanField('Visited', default=False)
    submit = SubmitField('Submit')