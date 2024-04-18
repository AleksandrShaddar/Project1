# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Task_2.html')


@app.route('/load', methods=['GET', 'POST'])
def load():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Файл {file_name}! Загружен'
    return render_template('Task_2.1.html')


if __name__ == "__main__":
    app.run()
    