# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше веб-приложение:
# ○ страницу "about"
# ○ страницу "contact".

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


if __name__ == "__main__":
    app.run()
    