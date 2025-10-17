from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class ProductForm(FlaskForm):
    type_p = StringField("Type", validators=[DataRequired(), Length(max=100)])
    designation_p = StringField("Désignation", validators=[DataRequired(), Length(max=255)])
    prix_ht = DecimalField("Prix HT", validators=[DataRequired()])
    date_in = DateField("Date d'entrée (YYYY-MM-DD)", validators=[DataRequired()])
    stock_p = IntegerField("Stock", default=0)
    submit = SubmitField("Enregistrer")