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
            logger.error(e)
            sys.exit()
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logger.info('Database connection closed.')

    
    #insert valores 
    def insert_many_values(self, query, values):
        """inser in SQL."""
        print(values)
        print(query)
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                cur.executemany(query, values )
                self.conn.commit()
                affected = f"{cur.rowcount} rows affected."
                cur.close()
                return affected
        except pymysql.MySQLError as e:
            logger.error(e)
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

    #inserta muchos valores de los simbolos a la bd
    def insert_valores_simbolo(self, valores):
        query = """INSERT INTO `merbal` (`simbolo`, `puntas_cantidad_compra`, `puntas_precio_compra`, `puntas_precio_venta`, `puntas_cantidad_venta`, `ultimo_precio`, `variacion_porcentual`, `apertura`, `maximo`, `minimo`, `ultimo_cierre`, `volumen`, `cantidad_operaciones`, `fecha`, `tipo_opcion`, `precio_ejercicio`, `fecha_vencimiento`, `mercado`, `moneda`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"""
        return self.insert_many_values(query, valores)