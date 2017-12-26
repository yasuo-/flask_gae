import logging

from flask import Flask
app = Flask(__name__)


@app.route('/')
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
