## forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, NumberRange

class RestaurantForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired(), Length(max=50)])
    location = StringField('location', validators=[DataRequired(), Length(max=100)])
    type = StringField('type', validators=[DataRequired(), Length(max=50)])

class ServiceForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired(), Length(max=200)])
    price = FloatField('price', validators=[DataRequired(), NumberRange(min=0)])

class CatboyForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired(), Length(max=50)])
    age = IntegerField('age', validators=[DataRequired(), NumberRange(min=0)])
    costume = StringField('costume', validators=[DataRequired(), Length(max=50)])
