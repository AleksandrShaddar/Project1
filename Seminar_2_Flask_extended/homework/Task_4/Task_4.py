# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

from flask import Flask, render_template, request, redirect


app = Flask(__name__)
app.secret_key = 'd21f208d497d37fb6c9578315ef3cffd805bb387c00210556fffbf4bc95de148'


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/submit', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        _message = request.form['mess']
        if _message:
            res = len(_message.split())
            return render_template('result.html', res=res)
        else:
            return redirect('/')
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
