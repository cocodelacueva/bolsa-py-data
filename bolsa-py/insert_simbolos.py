import config
from db import Database



def insert_simbolos(valores):
    query = "INSERT INTO `tit` (`name`, `prop`) VALUES ( "+valores+" )"
    # Create a new record
    # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    db = Database(config)
    insertSimbolos = db.run_query(query)
    print(insertSimbolos)