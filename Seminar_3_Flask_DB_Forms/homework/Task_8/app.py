# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе
# данных, а пароль должен быть зашифрован.


from flask import Flask, render_template, request, redirect
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
    if request.method == 'POST' and form.validate():
        user = Users(name=form.name.data,
                     sername=form.sername.data,
                     email=form.sername.data,
                     password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
