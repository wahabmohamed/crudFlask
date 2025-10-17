from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional

class ProfileForm(FlaskForm):
    first_name = StringField("Prénom", validators=[DataRequired(), Length(max=150)])
    last_name = StringField("Nom", validators=[DataRequired(), Length(max=150)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=150)])
    password = PasswordField("Nouveau mot de passe (optionnel)", validators=[Optional(), Length(min=6)])
    submit = SubmitField("Mettre à jour")