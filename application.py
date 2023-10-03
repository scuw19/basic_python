import json
import sys
import os 
import flask 

application = flask.Flask(__name__)

@application.route('/')
def hello_world():
    return flask.jsonify({
        'name': 'flaskapp',
        'python_version': sys.version.split(" ", 2)[0],
        'environment': os.environ.copy(),
        'flask_version': flask.__version__,
    })

if __name__ == '__main__':
    port = int(os.environ.get("FLASK_RUN_PORT", 8000))
    application.run(host='0.0.0.0', debug=False, port=port)
