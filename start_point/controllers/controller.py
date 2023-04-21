from flask import render_template, request, redirect
import datetime
from app import app
from models.event import *
from models.events import *

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods = ['POST'])
def add_event():
    date = request.form['date']
    split_date = date.split("-")
    date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    name = request.form['name']
    guests = request.form['guests']
    recurring = True if 'recurring' in request.form else False # will cause errors if not ticked hence else False is needed.
    room_location = request.form['room_location']
    description = request.form['description']
    new_event = Event(date, name, guests, recurring, room_location, description)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events) #add redirect here instead of render 

#add a function to delete an event
@app.route('/events/delete/<name>', methods =['POST'])
def delete_an_event_by_name(name):
    remove_event(name)
    return redirect('/events')
