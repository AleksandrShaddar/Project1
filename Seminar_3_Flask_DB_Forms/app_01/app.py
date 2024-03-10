from flask import Flask, render_template
from models import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_1.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-user")
def add_user():
    user = User(username='Alex', email='alex@mail.ru')
    db.session.add(user)
    db.session.commit()


@app.cli.command("del-user")
def del_user():
    user = User.query.filter_by(username='Alex').first()
    db.session.delete(user)
    db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
