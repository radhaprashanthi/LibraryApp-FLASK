from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(Form):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
