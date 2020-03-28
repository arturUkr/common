from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SubmitField
from wtforms.validators import DataRequired


class AddMarket(FlaskForm):

    market_name = StringField('Market name', validators=[DataRequired()])
    market_location = StringField('Market location', validators=[DataRequired()])
    market_img_name = FileField('Market_img_name', validators=[DataRequired()])
    market_submit = SubmitField('Add_market')
