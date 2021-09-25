from flask import Flask


app = Flask(__name__)

# define global constants
PORT=1337
FLASK_DEBUG=True


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/users/<string:user_id>/sync")
def sync_to_google_calendar():
    return "<p>I synced to google calendar</p>"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=FLASK_DEBUG)
