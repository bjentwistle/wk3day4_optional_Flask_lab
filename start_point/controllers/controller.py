from flask import render_template, request
from app import app
from models.events import events, add_new_event
from models.event import *

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods = ['POST'])
def add_event():
    date = request.form['date']
    name = request.form['name']
    guests = request.form['guests']
    recurring = request.form['recurring']
    room_location = request.form['room_location']
    description = request.form['description']
    new_event = Event(date, name, guests, recurring, room_location, description)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)
