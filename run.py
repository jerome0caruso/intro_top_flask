# from flask module import the class Flask
from flask import Flask
# setups the app
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route('/test')
def tester():
    return "This is a test yo!"

if __name__ == '__main__':
    app.run()