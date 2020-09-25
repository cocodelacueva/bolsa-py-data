from flask import Flask
from intervalos import insertSimbolosInDB
from dataprocess import getDataFromDBinsertinFirebase

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
    </ul>
    """

@app.route('/update-valores')
def updateMerbal():
    print('updating valores, every hour')
    insertSimbolosInDB()
    return 'updating valores'


@app.route('/update-firebase')
def updateFirebase():
    print('updating firestore, from or local mysqls')
    
    paneles = [
            {
                "mysql" : 'panel_general',
                "firestore":  'panel_general',
                "name" : "Panel General"
            },
            {
                "mysql" : 'panel_cedears',
                "firestore":  'panel_cedears',
                "name" : "CEDEARs"
            }
        ]
    dia = "2"#cuantos dias para atras busca

    getDataFromDBinsertinFirebase(paneles, dia)
    return 'firestore updated'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)