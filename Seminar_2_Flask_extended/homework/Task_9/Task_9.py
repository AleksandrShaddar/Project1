# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, render_template, request
from flask import url_for, redirect, session


app = Flask(__name__)
app.secret_key = 'c9bc73a467aabd6f3d519c58391e81247c14cc0b4628be97c419dbc78024980a'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        if request.form['mail'] and request.form['name']:
            _name = request.form.get('name')
            _mail = request.form.get('mail')
            session['username'] = [_name, _mail] or 'NoName'
            return redirect(url_for('hello', name=_name))
        else:
            return redirect('/')
    return render_template('base.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('welcome.html', name=name)


@app.route('/exit')
def exit_():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
