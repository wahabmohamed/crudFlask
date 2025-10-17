from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional

class UserForm(FlaskForm):
    username = StringField("Nom utilisateur", validators=[DataRequired(), Length(max=150)])
    first_name = StringField("Prénom", validators=[DataRequired(), Length(max=150)])
    last_name = StringField("Nom", validators=[DataRequired(), Length(max=150)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=150)])
    password = PasswordField("Mot de passe", validators=[Optional(), Length(min=6)])
    role = SelectField("Rôle", choices=[("user", "User"), ("admin", "Admin")])
    submit = SubmitField("Enregistrer")