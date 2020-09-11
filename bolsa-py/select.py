import config
from db import Database


def selectSimbolos():
    
    db = Database(config)
    simbolos = db.select_all('tit')
    print(simbolos)