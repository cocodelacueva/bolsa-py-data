from os import environ, path

basedir = path.abspath(path.dirname(__file__))
credentialsFirebase = path.join(basedir, "credentialsFirebase.json")
minutesInterval = 50

# paneles es cada instancia de valores, por ejemplo, acciones, cedears, merbal, merbal25, etc
# estos valores son tanto en mysql como firebase
paneles = [
    {
        "mysql" : 'panel_general',
        "firestore":  'panel_general',
        "name" : "Panel General",
        "default_limit": 250,
    },
    {
        "mysql" : 'panel_cedears',
        "firestore":  'panel_cedears',
        "name" : "CEDEARs",
        "default_limit": 800,
    }
]


# MYSQL Database config
db_user = environ.get('MYSQL_USER')
db_password = environ.get('MYSQL_PASSWORD')
db_host = environ.get('MYSQL_HOST')
db_port = int(environ.get('MYSQL_PORT'))
db_name = environ.get('MYSQL_DATABASE')

# API INVERTIR ONLINE CONFIG
apiUser = environ.get('API_USER')
apiPw = environ.get('API_PW')
urlApilBase = 'https://api.invertironline.com/api/v2/'
urlApiToken = 'https://api.invertironline.com/token'


# DEVELOP VARS DOCKER-COMPOSE FILE
# db_user = 'user'
# db_password = '123'
# db_host = 'localhost'
# db_port = 3320
# db_name = 'bolsa'
# apiUser = ''
# apiPw = ''
