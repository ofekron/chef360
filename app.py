import json

from flask import Flask, Blueprint, Response

from v1.api import blueprint as v1
from v2.api import blueprint as v2

app = Flask(__name__)
app.register_blueprint(v1)
app.register_blueprint(v2)

@app.errorhandler(404)
def index(p):
    return Response(json.dumps(['%s' % rule for rule in app.url_map.iter_rules()]), mimetype='application/json')
if __name__ == '__main__':
    app.run()