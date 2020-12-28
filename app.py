import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_view():
    return 'Index page'


@app.route('/all')
def all_teachers_view():
    return 'All teachers'


@app.route('/goals/<goal>/')
def goal_view(goal):
    return 'здесь будет цель <goal>'


@app.route('/profiles/<int:id>/')
def profile_view(id):
    with open('db.json', 'r', encoding='utf-8') as f:
        profiles = json.load(f)
    print(type(profiles))
    return render_template('profile.html', id=id, profiles=profiles)


@app.route('/request/')
def request_view():
    return 'здесь будет заявка на подбор'


@app.route('/request_done/')
def request_done_view():
    return 'заявка на подбор отправлена'


@app.route('/booking/<int:id>/<day>/<time>/')
def booking_view():
    return 'здесь будет форма бронирования <id учителя>'


@app.route('/booking_done/')
def booking_done_view():
    return 'заявка отправлена'


if __name__ == '__main__':
    app.run()
