import logging

from flask import Flask, render_template, request, make_response
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


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        res = request.args.get('get_value')
    elif request.method == 'POST':
        res = request.form['post_value']

    return res


@app.route('/post_request', methods=['POST'])
def post_request():
    username = request.form["username"]
    print(username)
    return username + 'Thank you'


@app.route('/post2/<post_id>', methods=['POST'])
def post(post_id):
    print(post_id)
    return 'Thanks post: id = %d' % post_id


# 型の指定もできる
@app.route('/post/<int:post_id>', methods=['POST'])
def post2(post_id):
    print(post_id)
    return 'Thanks post: id = %d' % post_id


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
