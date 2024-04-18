# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.

from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('Task_3.html')
LOGIN = 'admin'
PASS = '123'

@app.route('/')
def index():
    return render_template('Task_3.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == LOGIN and password == PASS:
            return render_template('Task_3.1.html')
    return render_template('Task_3.err.html')


if __name__ == "__main__":
    app.run()
    