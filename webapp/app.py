import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f'Hello world version {os.environ["version"]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
