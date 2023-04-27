from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class GoodsForm(FlaskForm):
    title = StringField('Название товара', validators=[DataRequired()])
    content = TextAreaField("Описание товара")
    price = StringField('Цена товара', validators=[DataRequired()])
    image = FileField('Изображение товара', validators=[DataRequired()])
    is_private = BooleanField("Авторский")
    submit = SubmitField('Применить')