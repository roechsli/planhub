import json
import time

from flask import Flask, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.dto.User import User

app = Flask(__name__)
engine = create_engine('mysql://root:passwort123@localhost:3306/planhub')

Session = sessionmaker(bind=engine)
session = Session()
# time.sleep(1)
# Session.configure(bind=engine)

# Session = sessionmaker()
# time.sleep(5)
# Session.configure(bind=engine)
# session = Session()

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
    # q = session.query(User, User.id, User.email)
    # database_fetch = session.execute(q)
    print("i am here")
    users = session.query(User)
    print("i am in step 2")
    # session.query(User).filter_by(name='ed').first()
    print(users)
    database_fetch = session.query(User).filter_by(id='user_id').first()
    print(database_fetch)
    # return json.dumps(database_fetch)
    return "database_fetch"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=FLASK_DEBUG)
