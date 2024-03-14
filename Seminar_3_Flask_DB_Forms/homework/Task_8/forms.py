from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from string import ascii_letters, digits


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    sername = StringField('Sername', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Введите корректный адрес!')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    conf_password = PasswordField('ConfirmPassword', validators=[EqualTo('password', message='Пароли должны совпадать')])

    def validate_password(self, password):
        status_char = False
        status_numb = False
        excluded_chars = ascii_letters
        excluded_numbs = digits
        for char in self.password.data:
            if char in excluded_chars:
                status_char = True
            if char in excluded_numbs:
                status_numb = True
        if status_char and status_numb:
            return True
        raise ValidationError(f"Пароль должен содержать минимум 1 цифру и 1 букву")
        return False
