from flask import Flask
from intervalos import insertSimbolosInDB, insertDolaresInDB, insertDigitalCoinsInDB
from dataprocess import insertLastSimbolsValuesInFirebase, getSimbolosNames, insertLastDolarsValuesInFirebase


app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>'App Bolsa PYthon MySQL!</h1>
    <h3>Routes:</h3>
    <ul>
        <li style="margin:20px 0;">
            <a href="http://192.168.0.160:8888/" target="_blank">
                ver phpmyadmin
            </a>
        </li>

        <li style="margin:20px 0;">
            <a href="/update-valores">
                /update-valores: from Api invertir online to mysql
            </a>
        </li>
       
        <li style="margin:20px 0;">
            <a href="/update-simbols-option">
                Actualiza el numbero de simbolos que sirve para actualizar firebase
            </a>
        </li>
        <li style="margin:20px 0;">
            <a href="/update-dolars">
                Actualiza la cotización de dolares
            </a>
        </li>
         <li style="margin:20px 0;">
            <a href="/update-digital-coins">
                Actualiza las monedas digitales
            </a>
        </li>
        <hr>
        <li style="margin:20px 0;">
            <a href="/update-firebase">
                /update-firebase: from mysql to firebase
            </a>
        </li>
        <li style="margin:20px 0;">
            <a href="/update-dolares-firebase">
                /update-dolares-firebase: from mysql to firebase
            </a>
        </li>
        
    </ul>
    """

@app.route('/update-valores')
def updateMerbal():
    print('updating valores, every hour')
    insertSimbolosInDB()
    return 'updating valores'

@app.route('/update-simbols-option')
def updateSimbolsNumbersByPanel():
    print('updating options simbols to know hoy many simbols are in any panel')
    getSimbolosNames()
    return 'simbols updated'

@app.route('/update-dolars')
def cotizacionesDolares():
    print('updating cotizaciones dolares')
    insertDolaresInDB()
    return 'dolares inserted in db'

@app.route('/update-digital-coins')
def cotizacionesMonedasDigitales():
    print('updating cotizaciones monedas digitales')
    return insertDigitalCoinsInDB()
    #return 'dolares updated'



#firebase:
@app.route('/update-firebase')
def updateFirebase():
    print('updating firestore, from or last records in local mysqls')
    insertLastSimbolsValuesInFirebase()
    return 'firestore updated'

@app.route('/update-dolares-firebase')
def updateDolaresFirebase():
    print('updating firestore dolares, from or last records in local mysqls')
    insertLastDolarsValuesInFirebase()
    return 'firestore dolares updated'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)