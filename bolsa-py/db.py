import sys
import pymysql
from loguru import logger

class Database:
    """Database connection class."""

    def __init__(self, config):
        self.host = config.db_host
        self.username = config.db_user
        self.password = config.db_password
        self.port = config.db_port
        self.dbname = config.db_name
        self.conn = None
    
    
    #open conection to database
    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                self.conn = pymysql.connect(
                    self.host,
                    user=self.username,
                    passwd=self.password,
                    db=self.dbname,
                    port=self.port,
                    connect_timeout=5
                )
        except pymysql.MySQLError as e:
            logger.error(e)
            sys.exit()
        finally:
            logger.info('Connection opened successfully.')

    

    #run a query like select
    def run_query(self, query):
        """Execute SQL query."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                if 'SELECT' in query:
                    records = []
                    cur.execute(query)
                    result = cur.fetchall()
                    for row in result:
                        records.append(row)
                    cur.close()
                    return records

                result = cur.execute(query)
                self.conn.commit()
                affected = f"{cur.rowcount} rows affected."
                cur.close()
                return affected
        except pymysql.MySQLError as e:
            logger(e)
            sys.exit()
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logger.info('Database connection closed.')

    
    #Selecciona todas las row de la tabla pasada
    def select_all(self, table):

        query = 'SELECT * FROM ' + table
        return self.run_query(query)
