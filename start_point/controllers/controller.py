from flask import render_template
from app import app
from models.events import events 
from models.event import *

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

