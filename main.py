import logging

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    s = "abc"
    lis = ["a1", "a2", "a3"]
    dic = {"name": "make", "age": 24}
    bl = True

    return render_template('index.html', str=s, lis=lis, dic=dic, bl=bl)


@app.route('/hello')
def hello_world():
    return 'Hello World!!!!!!!!!!!!'


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    app.debug = True
    app.run()
