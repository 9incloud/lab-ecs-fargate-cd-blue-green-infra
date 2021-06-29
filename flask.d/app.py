from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to flask framework'


@app.route('/delay')
def deploy():
    time.sleep(3)
    return 'Delay api for test'


@app.route('/v1/hello')
def health_check():
    return 'ok'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
