from flask import Flask

app = Flask(__name__)


@app.route('/')
def index_view():
    return 'Index page'


@app.route('/all')
def all_teachers_view():
    return 'All teachers'


if __name__ == '__main__':
    app.run()
