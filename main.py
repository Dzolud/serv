from data import db_session, news_api
from flask import Flask


app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


def main():
    db_session.global_init("db/users.db")
    app.register_blueprint(news_api.blueprint)
    app.run(port=5000, host='127.0.0.1')


if __name__ == '__main__':
    main()
