import os

from flask import Flask, Response

app = Flask(__name__)

@app.route('/', endpoint='healthz')
def get_version():
    return Response()

@app.route('/version', endpoint='get_version')
def get_version():
    return os.environ['version']

if __name__ == '__main__':
    app.run(host='0.0.0.0')
