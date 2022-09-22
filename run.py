from flask import Flask
from datetime import datetime
import pytz
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    timezone_NY = pytz.timezone('America/New_York') 
    dt_NY = datetime.now(timezone_NY)
    return dt_NY.strftime("%H:%M:%S")

app.run(host='0.0.0.0',
        port=8000,
        debug=True)
