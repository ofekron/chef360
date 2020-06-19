import json

from flask import Flask, Blueprint, Response
from werkzeug.utils import redirect

from utils import version
from v1.api import blueprint as v1
from v2.api import blueprint as v2





app = Flask(__name__)
app.register_blueprint(v1)
app.register_blueprint(v2)
latest=v2
@app.route('/')
def redirect_main():
    return redirect(f"/api/{latest.name}/docs/", code=302)

@app.route('/api/latest/docs/')
def redirect_latest():
    return redirect(f"/api/{latest.name}/docs/", code=302)


@app.errorhandler(404)
def index(p):
    return Response(json.dumps(['%s' % rule for rule in app.url_map.iter_rules()]), mimetype='application/json')
if __name__ == '__main__':
    app.run()