# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

from flask import Flask, render_template, request, redirect, flash


app = Flask(__name__)
app.secret_key = 'd21f208d497d37fb6c9578315ef3cffd805bb387c00210556fffbf4bc95de148'


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/submit', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        _name = request.form['name']
        if _name:
            flash(f'Привет {_name}!')
            return render_template('hello.html')
        else:
            flash('Введите имя!')
            return redirect('/')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
