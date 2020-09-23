from flask import Flask
from intervalos import intervaloUpdatingMerval
from dataprocess import getDataFromDBinsertinFirebase

app = Flask(__name__)

@app.route('/')
def index():
    return 'App Bolsa PYthon MySQL. 1Route: /update-valores || /update-firebase'

@app.route('/update-valores')
def updateMerbal():
    print('updating valores, for 7 hours')
    intervaloUpdatingMerval()
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