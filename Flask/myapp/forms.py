#forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class CityForm(FlaskForm):
    cityName = StringField('City Name', validators=[DataRequired()])
    cityRank = IntegerField('City Rank')
    visited = BooleanField('Visited')
    submit = SubmitField('Submit')