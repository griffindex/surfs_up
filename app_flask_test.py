# import Flask dependency

from flask import Flask


# Create a new Flask app instance
app = Flask(__name__)


# Create Flask routes
@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/code')
def skill_drill():
    return 'Okay'
