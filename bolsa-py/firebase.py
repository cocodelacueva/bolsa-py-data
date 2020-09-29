## clase firebase con para crear y administrar los datos
import firebase_admin
from firebase_admin import credentials, firestore

class Firestore:
    """Database connection class."""

    def __init__(self, config):
        self.credentialsFirebase = config.credentialsFirebase
        

    # inicializa las credenciales
    def initCredentials(self):

        # inicializa firestore que vamos a utilizar ahora
        cred = credentials.Certificate( self.credentialsFirebase )
        defaultApp = firebase_admin.initialize_app(cred)

        db = firestore.client()
        return db

    ##agregar data
    def addDoc(self, doc, collection):
        if firebase_admin._DEFAULT_APP_NAME in firebase_admin._apps:
            print('firebase ya inicializada')
            app = firebase_admin.get_app()
            db = firestore.client()
        else:
            db = self.initCredentials()

        #data, ejemplo
        # nuevousuario = {
        #     'uid': 'fdsafd', 'email': 'miemail@gmail.com'
        # }

        resp = db.collection(collection).add(doc)
        return resp

    ## leer data
    def getCollectionAll(self, collection):
        db = self.initCredentials()

        collection = list( db.collection(collection).get())
        valores = []

        for doc in collection:
            valores.append(doc.to_dict())

        return valores