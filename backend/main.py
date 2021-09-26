import simplejson as json
import datetime
import logging
from datetime import timedelta
import decimal

from flask import Flask, request
from flask_cors import CORS, cross_origin
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
from events_calendarAPI import create_event, tasklist_calendar_scheduler

# define Flask variables
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# define database variables
engine = create_engine(MYSQL_CONNECTION_STRING, echo=True)
metadata = MetaData()
metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# define global constants
PORT = 1337
FLASK_DEBUG = True

# define global google constants
service = calendarservice()

# Global logger
logger = logging.getLogger(__name__)


@cross_origin()
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@cross_origin()
@app.route("/users/<string:user_id>/sync")
def sync_to_google_calendar(user_id: str):
    tasks = get_user_tasks(user_id)
    name = get_user_name(user_id)
    file_dict = json.loads(tasks)

    tasklist_calendar_scheduler(file_dict, get_user_name(user_id), service)
    return "<p>Tasks are now synced to google calendar for </p>" + name


@cross_origin()
@app.route("/tasks/<string:task_id>", methods=["POST", "GET"])
def get_or_add_new_task(task_id: str):
    if request.method == 'POST':
        # create or update task
        task = request.form['task']
        return "sorry function not implemented yet"
    else:
        # get task
        result = session.query(Task).filter_by(id=task_id)
        return json.dumps([item.json() for item in result], cls=DecimalEncoder)


@cross_origin()
@app.route("/users/<string:user_id>")
def get_user(user_id: str):
    # query database for user_id
    result = session.query(User).filter_by(id=user_id)
    return json.dumps([item.json() for item in result], cls=DecimalEncoder)


@cross_origin()
@app.route("/settings/<string:setting_id>")
def get_settings(setting_id: str):
    # query database for setting_id
    result = session.query(Settings).filter_by(id=setting_id)
    return json.dumps([item.json() for item in result], cls=DecimalEncoder)


@cross_origin()
@app.route("/users/<string:user_id>/settings")
def get_user_settings(user_id: str):
    # query database for user_id
    result = session.query(Settings).filter_by(user_id=user_id)
    return json.dumps([item.json() for item in result], cls=DecimalEncoder)



@app.route("/users/<string:user_id>/tasks")
def get_user_tasks(user_id: str):
    # query database for user_id
    result = session.query(Task).filter((Task.user_id == user_id) | (Task.guests == user_id))
    # TODO allow also several guests
    result = [item.json() for item in result]
    result = filter_tasks(result)
    return json.dumps(result, iterable_as_array=True)


def filter_tasks(tasks: list):
    return_tasks = []
    for task in tasks:
        filtered_task = dict()
        filtered_task["start"] = dict()

        # convert this to datetime object
        f = '%Y-%m-%d %H:%M:%S'
        filtered_task["start"]["dateTime"] = datetime.datetime.strptime(task["start_time"], f) if task[
                                                                                                      "start_time"] is not None else None
        filtered_task["start"]["timeZone"] = "GMT+2"
        # calculate end-time
        filtered_task["duration_mins"] = task["duration"] * MINUTE_TIME_UNIT_MULTIPLIER[task["duration_unit"]]
        filtered_task["end"] = dict()
        filtered_task["end"]["dateTime"] = task["start_time"] + timedelta(minutes=filtered_task["duration_mins"]) if \
        task["start_time"] is not None and filtered_task["duration_mins"] is not None else None
        filtered_task["end"]["timeZone"] = "GMT+2"

        filtered_task["summary"] = task["name"]
        filtered_task["description"] = task["description"]
        # only allow google visibility settings
        filtered_task["visibility"] = task["visibility"] if task["visibility"] in ["private", "default",
                                                                                   "public"] else None
        filtered_task["priority"] = task["priority"]
        filtered_task["location"] = task["location"]
        # TODO not implemented yet (join on recurrence table to get pattern)
        filtered_task["recurrence"] = None

        return_tasks.append(filtered_task)
    return return_tasks


def get_user_name(user_id: str) -> str:
    # query database for user_id
    result = session.query(User).filter((User.id == user_id)).one()
    if result is not None:
        return result.first_name + " " + result.last_name
    return ""

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self).default(o)


if __name__ == '__main__':
    # file1 = get_user_tasks('1')
    # file_dict1 = json.loads(file1)

    # file2 = get_user_tasks('2')
    # file_dict2 = json.loads(file2)

    # tasklist_calendar_scheduler(file_dict1, get_user_name('1'), service)
    # tasklist_calendar_scheduler(file_dict2, get_user_name('2'), service)

    app.run(host='0.0.0.0', port=PORT, debug=FLASK_DEBUG)
