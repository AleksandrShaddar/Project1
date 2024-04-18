# Задача 8.
# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.

# Задача 9.
# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)

_shoes = [{'name': 'Кросовки',
           'size': '41',
           'price': '8500',
           },
          {'name': 'Туфли',
           'size': '42',
           'price': '7000',
           }]

_clothes = [{'name': 'Пальто',
             'size': '52',
             'price': '9000',
             },
            {'name': 'Рубашка',
             'size': '48',
             'price': '3500',
             }]


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/clothes')
def clothes():
    return render_template('clothes.html', clothes=_clothes)


@app.route('/shoes')
def shoes():
    return render_template('shoes.html', shoes=_shoes)


if __name__ == "__main__":
    app.run()
