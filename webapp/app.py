import os

from flask import Flask

app = Flask(__name__)

@app.route('/version', endpoint='get_version')
def get_version():
    return f'Hello aaa {os.environ["version"]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
