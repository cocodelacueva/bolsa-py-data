## clase firebase con para crear y administrar los datos
import firebase_admin
from firebase_admin import credentials, firestore

class Firestore:
    """Database connection class."""

    def __init__(self, config):
        self.credentialsFirebase = config.credentialsFirebase
        self.initialize = False
        self.cred = credentials.Certificate( self.credentialsFirebase )
        self.defaultApp = firebase_admin.initialize_app(self.cred)

    # inicializa las credenciales
    def initCredentials(self):

        # inicializa firestore que vamos a utilizar ahora
        db = firestore.client()
        return db

    ##agregar data
    def addDoc(self, doc, collection):
        
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