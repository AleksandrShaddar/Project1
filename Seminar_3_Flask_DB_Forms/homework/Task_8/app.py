# Задача 8.
# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе
# данных, а пароль должен быть зашифрован.

# Задача 7.
# Создайте форму регистрации пользователей в приложении Flask. Форма должна
# содержать поля: имя, фамилия, email, пароль и подтверждение пароля. При отправке
# формы данные должны валидироваться на следующие условия:
# - Все поля обязательны для заполнения.
# - Поле email должно быть валидным email адресом.
# - Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и
# одну цифру.
# - Поле подтверждения пароля должно совпадать с полем пароля.
# - Если данные формы не прошли валидацию, на странице должна быть выведена
# соответствующая ошибка.
# - Если данные формы прошли валидацию, на странице должно быть выведено
# сообщение об успешной регистрации.


from flask import Flask, render_template, request, redirect, flash
from models import db, Users
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b3f62186ef283e9072b300596bda5cdaf0a612a1687987a8070d0ad400468f3b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_08.db'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate() and form.validate_password(form.password.data):
        user = Users(name=form.name.data,
                     sername=form.sername.data,
                     email=form.email.data,
                     password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash('Регистрация прошла успешно!')
        return redirect('/')
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
