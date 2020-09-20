from flask import Flask
from intervalos import intervaloUpdatingMerval

app = Flask(__name__)

@app.route('/')
def index():
    return 'App Bolsa PYthon MySQL. 1Route: /update-valores'

@app.route('/update-valores')
def updateMerbal():
    print('updating valores, for 7 hours')
    intervaloUpdatingMerval()
    return 'updating valores'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)