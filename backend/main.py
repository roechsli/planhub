import json
import datetime
from datetime import timedelta

from flask import Flask, request
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from dto.User import User
from dto.Task import Task
from dto.Settings import Settings
from credentials import MYSQL_CONNECTION_STRING
from consts import MINUTE_TIME_UNIT_MULTIPLIER
from Google import Create_Service, convert_to_RFC_datetime
from insert_delete_calendar import calendarservice, create_calendar, delete_calendar
from change_calendar_color import get_color_profiles, change_color_profile
from update_calendar import find_cal_summary, update_calendar
from events_calendarAPI import create_event


# define Flask variables
app = Flask(__name__)

# define database variables
engine = create_engine(MYSQL_CONNECTION_STRING, echo = True)
metadata = MetaData()
metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# define global constants
PORT = 1337
FLASK_DEBUG = True

# define global google constants
service = calendarservice()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/users/<string:user_id>/sync")
def sync_to_google_calendar(user_id: str):
    return "<p>Not yet synced to google calendar for </p>" + user_id


@app.route("/tasks/<string:task_id>", methods=["POST", "GET"])
def get_or_add_new_task(task_id: str):
    if request.method == 'POST':
        # create or update task
        task = request.form['task']
        return "sorry function not implemented yet"
    else:
        # get task
        result = session.query(Task).filter_by(id=task_id)
        return json.dumps([item.json() for item in result])


@app.route("/users/<string:user_id>")
def get_user(user_id: str):
    # query database for user_id
    result = session.query(User).filter_by(id=user_id)
    return json.dumps([item.json() for item in result])


@app.route("/settings/<string:setting_id>")
def get_settings(setting_id: str):
    # query database for setting_id
    result = session.query(Settings).filter_by(id=setting_id)
    return json.dumps([item.json() for item in result])


@app.route("/users/<string:user_id>/settings")
def get_user_settings(user_id: str):
    # query database for user_id
    result = session.query(Settings).filter_by(user_id=user_id)
    return json.dumps([item.json() for item in result])


@app.route("/users/<string:user_id>/tasks")
def get_user_tasks(user_id: str):
    # query database for user_id
    result = session.query(Task).filter((Task.user_id == user_id) | Task.guests == user_id)
    # TODO allow also several guests
    result = [item.json() for item in result]
    result = filter_tasks(result)
    return json.dumps(result)


def filter_tasks(tasks: list):
    return_tasks = []
    for task in tasks:
        filtered_task = {}
        filtered_task["start"] = {}
        # convert this to datetime object
        f = '%Y-%m-%d %H:%M:%S'
        filtered_task["start"]["dateTime"] = datetime.datetime.strptime(task["start_time"], f) if task["start_time"] is not None else None
        filtered_task["start"]["timeZone"] = "GMT+2"
        # calculate end-time
        duration_mins = task["duration"] * MINUTE_TIME_UNIT_MULTIPLIER[task["duration_unit"]]
        filtered_task["end"] = {}
        filtered_task["end"]["dateTime"] = datetime.datetime.strptime(task["end_time"], f) if task["end_time"] is not None else task["start_time"] + timedelta(minutes=duration_mins) if task["start_time"] is not None and duration_mins is not None else None
        filtered_task["end"]["timeZone"] = "GMT+2"
        
        filtered_task["summary"] = task["name"]
        filtered_task["description"] = task["description"]
        # only allow google visibility settings
        filtered_task["visibility"] = task["visibility"] if task["visibility"] in ["private", "default", "public"] else None
        filtered_task["priority"] = task["priority"]
        filtered_task["location"] = task["location"]
        # TODO not implemented yet (join on recurrence table to get pattern)
        filtered_task["recurrence"] = None
        
        return_tasks.append(filtered_task)
    return return_tasks


if __name__ == '__main__':
    print('main')
    create_calendar('PlanHubCalendar 2', service)
    get_color_profiles(service)
    myCalendar = find_cal_summary(service, 'PlanHubCalendar 2')
    update_calendar(service, myCalendar, 'PlanHubCalendar 2', 'Alices Calendar', 'Zurich')

    """
    Create an event
    """

    hour_adjustment = 2
    event_request_body = {
        'start': {
            'dateTime': convert_to_RFC_datetime(2021, 11, 1, 12 + hour_adjustment, 30),
            'timeZone': 'GMT+2'
        },
        'end': {
            'dateTime': convert_to_RFC_datetime(2021, 11, 1, 14 + hour_adjustment, 30),
            'timeZone': 'GMT+2'
        },
        'summary': 'Finish Q3 report',
        'description': 'lalala',
        'colorId': 5,
        'status': 'confirmed',
        'transparency': 'opaque',
        'visibility': 'private',
        'location': 'Zurich, Zurich',
        'recurrence': None
    }
    create_event(service, myCalendar, event_request_body)

    app.run(host='0.0.0.0', port=PORT, debug=FLASK_DEBUG)
