from bottle import Bottle, run
from routing import setup_routing
from db import setup_db
from db_data import seed_db


app = Bottle()

app.route()

setup_db(app)
seed_db(app)
setup_routing(app)

run(app, host='localhost', port=8080, debug=True)
