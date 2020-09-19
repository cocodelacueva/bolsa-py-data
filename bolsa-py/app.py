from flask import Flask
from intervalos import intervaloUpdatingMerval

app = Flask(__name__)

@app.route('/')
def index():
    return 'App Bolsa PYthon MySQL. 1Route: /update-merval'

@app.route('/update-merval')
def updateMerbal():
    print('updating merval, for 7 hours')
    intervaloUpdatingMerval()
    return 'updating Merval'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)