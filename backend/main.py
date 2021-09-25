import json
import time

from flask import Flask, request, redirect, url_for
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dto.User import User
from credentials import MYSQL_CONNECTION_STRING

from insert_delete_calendar import calendarservice, create_calendar, delete_calendar

# define global google constants
service = calendarservice()
create_calendar('PlanHubCalendar 2', service)

# define global flask constants
app = Flask(__name__)

engine = create_engine(MYSQL_CONNECTION_STRING)
metadata = MetaData()
users_table = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String),
)
metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# define global constants
PORT = 1337
FLASK_DEBUG = True


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/users/<string:user_id>/sync")
def sync_to_google_calendar(user_id: str):
    return "<p>I synced to google calendar for </p>" + user_id


@app.route("/users/tasks/<string:task_id>", methods=["POST", "GET"])
def get_or_add_new_task(user_id: str, task_id: str):
    if request.method == 'POST':
        # create or update task
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        # get task
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route("/users/<string:user_id>")
def get_user(user_id: str):
    # query database for user_id
    result = session.query(User).all()
    return json.dumps([item.json() for item in result])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=FLASK_DEBUG)
