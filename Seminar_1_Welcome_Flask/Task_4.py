# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/about/')
def about():
    return 'Информация о нашем веб-приложении.'


@app.route('/contact/')
def contact():
    return 'Контакты'


@app.route('/summa/<int:num_1>/<int:num_2>')
def summa(num_1, num_2):    
    return f'Сумма чисел: {num_1 + num_2}'


@app.route('/length/<string:text>/')
def length_text(text):
    return f'Длина строки {len(text)} символа(ов)'


if __name__ == "__main__":
    app.run()
    