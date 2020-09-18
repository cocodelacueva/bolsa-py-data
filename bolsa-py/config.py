from os import environ, path
#from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))

# Database config
# db_user = environ.get('MYSQL_USER')
# db_password = environ.get('MYSQL_PASSWORD')
# db_host = environ.get('MYSQL_HOST')
# db_port = environ.get('MYSQL_PORT')
# db_name = environ.get('MYSQL_DATABASE')
# apiUser = environ.get('API_USER')
# apiPw = environ.get('API_PW')
# urlApilBase = environ.get('API_URL_BASE')
# urlApiToken = environ.get('API_URL_TOKEN')
db_user = 'user'
db_password = '123'
db_host = 'localhost'
db_port = 3320
db_name = 'bolsa'
apiUser = ''
apiPw = ''
urlApilBase = 'https://api.invertironline.com/api/v2/'
urlApiToken = 'https://api.invertironline.com/token'