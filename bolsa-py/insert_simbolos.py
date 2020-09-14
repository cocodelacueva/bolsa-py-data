import config
from db import Database


def insert_simbolos(valores):
    query = "INSERT INTO `merbal` (`simbolo`, `puntas_cantidad_compra`, `puntas_precio_compra`, `puntas_precio_venta`, `puntas_cantidad_venta`, `ultimo_precio`, `variacion_porcentual`, `apertura`, `maximo`, `minimo`, `ultimo_cierre`, `volumen`, `cantidad_operaciones`, `fecha`, `tipo_opcion`, `precio_ejercicio`, `fecha_vencimiento`, `mercado`, `moneda`) VALUES ( "+valores+" )"
    # Create a new record
    # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    db = Database(config)
    insertSimbolos = db.run_query(query)
    print(insertSimbolos)