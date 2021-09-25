from flask import Flask
import json

from insert_delete_calendar import calendarservice, create_calendar, delete_calendar

# define global google constants
service = calendarservice()
create_calendar('PlanHubCalendar 2', service)

# define global flask constants
app = Flask(__name__)

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
    app.run(host='0.0.0.0', port=PORT, debug=FLASK_DEBUG)
