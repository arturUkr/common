from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class AddProduct(FlaskForm):
    product_name = StringField('Product_name', validators=[DataRequired()])
    product_description = StringField('Product_description', validators=[DataRequired()])
    product_img_name = FileField('Product_img_name', validators=[DataRequired()])
    product_price = StringField('Product_price', validators=[DataRequired()])
    submit = SubmitField('Add_product')
