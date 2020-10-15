from flask import Flask
from intervalos import insertSimbolosInDB, insertDolaresInDB
from dataprocess import insertLastSimbolsValuesInFirebase, getSimbolosNames


app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>'App Bolsa PYthon MySQL!</h1>
    <h3>Routes:</h3>
    <ul>
        <li>
            <a href="/update-valores">
                /update-valores: from Api invertir online to mysql
            </a>
        </li>
        <li>
            <a href="/update-firebase">
                /update-firebase: from mysql to firebase
            </a>
        </li>
        <li>
            <a href="http://192.168.0.160:8888/" target="_blank">
                ver phpmyadmin
            </a>
        </li>
        <li>
            <a href="/update-simbols-option">
                Actualiza el numbero de simbolos que sirve para actualizar firebase
            </a>
        </li>
        <li>
            <a href="/update-dolars">
                Actualiza la cotización de dolares
            </a>
        </li>
        
    </ul>
    """

@app.route('/update-valores')
def updateMerbal():
    print('updating valores, every hour')
    insertSimbolosInDB()
    return 'updating valores'


@app.route('/update-firebase')
def updateFirebase():
    print('updating firestore, from or last records in local mysqls')
    insertLastSimbolsValuesInFirebase()
    return 'firestore updated'

@app.route('/update-simbols-option')
def updateSimbolsNumbersByPanel():
    print('updating options simbols to know hoy many simbols are in any panel')
    getSimbolosNames()
    return 'simbols updated'

@app.route('/update-dolars')
def cotizacionesDolares():
    print('updating cotizaciones dolares')
    return insertDolaresInDB()
    #return 'dolares updated'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)