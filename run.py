from datetime import datetime
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return date_time

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
