from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    sername = StringField('Sername', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Введите корректный адрес!')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    conf_password = PasswordField('ConfirmPassword', validators=[EqualTo('password', message='Пароли должны совпадать')])