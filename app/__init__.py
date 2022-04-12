from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello():
    return 'Hello world'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
