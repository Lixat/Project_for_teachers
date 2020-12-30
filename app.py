from json import load, dump
from random import randint

from flask import Flask, render_template, request

app = Flask(__name__)

week = {
    'mon': 'Понедельник',
    'tue': 'Вторник',
    'wed': 'Среда',
    'thu': 'Четверг',
    'fri': 'Пятница',
    'sat': 'Суббота',
    'sun': 'Воскресенье'
}


@app.route('/')
def index_view():
    with open('db.json', 'r') as f:
        data = load(f)
    teachers = []
    while len(teachers) < 6:
        teacher = data['teachers'][randint(0, 11)]
        if teacher not in teachers:
            teachers.append(teacher)
    goals = data['goals']
    return render_template('index.html', teachers=teachers, goals=goals)


@app.route('/all')
def all_teachers_view():
    with open('db.json', 'r') as f:
        data = load(f)
    all = data['teachers']
    return render_template('all.html', all=all)


@app.route('/goals/<goal>/')
def goal_view(goal):
    with open('db.json', 'r') as f:
        data = load(f)
    teachers = data['teachers']
    profile = [teacher for teacher in teachers if goal in teacher['goals']]
    goals = data['goals']
    return render_template('goal.html', profile=profile, goal=goals[goal])


@app.route('/profiles/<int:id>/')
def profile_view(id):
    with open('db.json', 'r', encoding='utf-8') as f:
        data = load(f)
    profile = data['teachers'][id]
    goals_for = data['goals']
    return render_template('profile.html', profile=profile, goals_for=goals_for, week=week)


@app.route('/request/')
def request_view():
    with open('db.json', 'r') as f:
        data = load(f)
    goals = data['goals']
    return render_template('request.html', goals=goals)


@app.route('/request_done/', methods=['POST'])
def request_done_view():
    goal = request.form['goal']
    time = request.form['time']
    name = request.form['username']
    phone = request.form['userphone']
    info = {
        'goal': goal,
        'time': time,
        'name': name,
        'phone': phone
    }
    with open('request.json', 'r') as f:
        data = load(f)
    data.append(info)
    with open('request.json', 'w') as f:
        dump(data, f)
    return render_template('request_done.html', info=info)


@app.route('/booking/<int:id>/<day>/<time>/')
def booking_view(id, day, time):
    with open('db.json', 'r') as f:
        data = load(f)
    profile = data['teachers'][id]
    day = day
    time = time
    return render_template('booking.html', profile=profile, day=day, time=time, week=week)


@app.route('/booking_done/', methods=['POST'])
def booking_done_view():
    id = request.form['clientTeacher']
    day = request.form['clientWeekday']
    time = request.form['clientTime']
    client_name = request.form['clientName']
    client_phone = request.form['clientPhone']
    order = {
        'id': id,
        'day': day,
        'time': time,
        'client_name': client_name,
        'client_phone': client_phone
    }
    with open('booking.json', 'r') as f:
        data = load(f)
    data.append(order)
    with open('booking.json', 'w') as f:
        dump(data, f)
    return render_template('booking_done.html', order=order, week=week)


if __name__ == '__main__':
    app.run()
