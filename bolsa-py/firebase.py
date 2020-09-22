## archivo de testing para firebase y firecloud
# funciona con firebase_admin que permite autorizar al servidor administrar firebase y sus apps como si fuera un usuario pero como super admin
# viene bien para este tipo de proyectos
# las credenciales estan en un archivo json, se realiza desde la consola de google firebase (ver readme)

from config import credentialsFirebase
import firebase_admin
from firebase_admin import credentials, firestore

# inicializa las credenciales
cred = credentials.Certificate( credentialsFirebase )
defaultApp = firebase_admin.initialize_app(cred)

# inicializa firestore que vamos a utilizar ahora
db = firestore.client()

##agregar data
nuevousuario = {
    'uid': 'fdsafd', 'email': 'miemail@gmail.com'
}

db.collection(u'usuarios').add(nuevousuario)

## leer data
users = list(db.collection(u'usuarios').get())

for user in users:
    print(user.to_dict())