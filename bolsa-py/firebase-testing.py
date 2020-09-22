## archivo de testing para firebase y firecloud
# funciona con firebase_admin que permite autorizar al servidor administrar firebase y sus apps como si fuera un usuario pero como super admin
# viene bien para este tipo de proyectos
# las credenciales estan en un archivo json, se realiza desde la consola de google firebase (ver readme)

# from config import credentialsFirebase
# import firebase_admin
# from firebase_admin import credentials, firestore

# # inicializa las credenciales
# cred = credentials.Certificate( credentialsFirebase )
# defaultApp = firebase_admin.initialize_app(cred)

# # inicializa firestore que vamos a utilizar ahora
# db = firestore.client()

# ##agregar data
# nuevousuario = {
#     'uid': 'fdsafd', 'email': 'miemail@gmail.com'
# }

# db.collection(u'usuarios').add(nuevousuario)

# ## leer data
# users = list(db.collection(u'usuarios').get())

# for user in users:
#     print(user.to_dict())


import config
from firebase import Firestore

fb = Firestore(config)

titulo = {
    
    "titulos" : [
            {
            "simbolo": "ALUA",
            "puntas": {
                "cantidadCompra": 80.0,
                "precioCompra": 48.700,
                "precioVenta": 49.800,
                "cantidadVenta": 200.0
            },
            "ultimoPrecio": 49.500,
            "variacionPorcentual": 0.81,
            "apertura": 49.000,
            "maximo": 49.600,
            "minimo": 48.200,
            "ultimoCierre": 49.500,
            "volumen": 427110.0,
            "cantidadOperaciones": 812.0,
            "fecha": "2020-09-08T17:00:04.807",
            "tipoOpcion": None,
            "precioEjercicio": None,
            "fechaVencimiento": None,
            "mercado": "BCBA",
            "moneda": "AR$"
            },
            {
            "simbolo": "BBAR",
            "puntas": {
                "cantidadCompra": 1000.0,
                "precioCompra": 141.050,
                "precioVenta": 150.000,
                "cantidadVenta": 230.0
            },
            "ultimoPrecio": 142.800,
            "variacionPorcentual": 0.52,
            "apertura": 139.900,
            "maximo": 143.000,
            "minimo": 137.000,
            "ultimoCierre": 142.800,
            "volumen": 91732.0,
            "cantidadOperaciones": 390.0,
            "fecha": "2020-09-08T17:00:05.617",
            "tipoOpcion": None,
            "precioEjercicio": None,
            "fechaVencimiento": None,
            "mercado": "BCBA",
            "moneda": "AR$"
            },
            {
            "simbolo": "BMA",
            "puntas": {
                "cantidadCompra": 300.0,
                "precioCompra": 229.000,
                "precioVenta": 239.050,
                "cantidadVenta": 2.0
            },
            "ultimoPrecio": 235.650,
            "variacionPorcentual": -1.60,
            "apertura": 236.000,
            "maximo": 238.600,
            "minimo": 230.000,
            "ultimoCierre": 235.650,
            "volumen": 386335.0,
            "cantidadOperaciones": 1057.0,
            "fecha": "2020-09-08T17:00:04.807",
            "tipoOpcion": None,
            "precioEjercicio": None,
            "fechaVencimiento": None,
            "mercado": "BCBA",
            "moneda": "AR$"
            }
        ]
    }

# fb.addDoc(titulo, u'titulos')
collection = fb.getCollectionAll(u'titulos')

for doc in collection:
    print(doc['titulos'][0])