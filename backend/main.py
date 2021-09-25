from flask import Flask
from pprint import pprint
import json
from Google import Create_Service, convert_to_RFC_datetime
from insert_delete_calendar import calendarservice, create_calendar, delete_calendar
from change_calendar_color import get_color_profiles, change_color_profile
from update_calendar import find_cal_summary, update_calendar

service = calendarservice()

app = Flask(__name__)
print('all')

# define global constants
PORT = 1337
FLASK_DEBUG = True


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/users/<string:user_id>/sync")
def sync_to_google_calendar(user_id: str):
    return "<p>I synced to google calendar for </p>" + user_id


@app.route("/users/<string:user_id>")
def get_user(user_id: str):
    # query database for user_id
    database_fetch = {
        "name": "database.user_id.name",
        "age": 45
    }
    return json.dumps(database_fetch)


if __name__ == '__main__':
    print('main')
    create_calendar('PlanHubCalendar 2', service)
    get_color_profiles(service)
    myCalendar = find_cal_summary(service, 'PlanHubCalendar 2')
    update_calendar(service, myCalendar, 'PlanHubCalendar 2', 'Alices Calendar', 'Zurich')

    """
    Create an event
    """
    colors = service.colors().get().execute()
    pprint(colors)

    hour_adjustment = 2
    event_request_body = {
        'start': {
            'dateTime': convert_to_RFC_datetime(2021, 11, 1, 12 + hour_adjustment, 30),
            'timeZone': 'GMT+2'
        },
        'end': {
            'dateTime': convert_to_RFC_datetime(2020, 11, 1, 14 + hour_adjustment, 30),
            'timeZone': 'GMT+2'
        },
        'summary': 'Finish Q3 report',
        'description' : 'lalala',
        'colorId': 5,
        'status': 'confirmed',
        'transparency': 'opaque',
        'visibility': 'private',
        'location': 'Zurich, Zurich'
    }

    app.run(host='0.0.0.0', port=PORT, debug=FLASK_DEBUG)


