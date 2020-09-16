import os
import config
from db import Database
import json


#inserta todos los elementos del json en la bd

db = Database(config)

with open(config.basedir+"/valores.json") as json_file:
    data = json.load(json_file)
    print(data['titulos'][0]['fecha'] )
    valores = []

    for simbolo in data['titulos']:

        valor = (simbolo['simbolo'], simbolo['puntas']['cantidadCompra'], simbolo['puntas']['precioCompra'], simbolo['puntas']['precioVenta'], simbolo['puntas']['cantidadVenta'], simbolo['ultimoPrecio'], simbolo['variacionPorcentual'], simbolo['apertura'], simbolo['maximo'], simbolo['minimo'], simbolo['ultimoCierre'], simbolo['volumen'], simbolo['cantidadOperaciones'], simbolo['fecha'], simbolo['tipoOpcion'], simbolo['precioEjercicio'], simbolo['fechaVencimiento'], simbolo['mercado'], simbolo['moneda'])

        valores.append(valor)
        
    queryResponse = db.insert_valores_simbolo(valores)
        




# Actividad repetitiva:

# import schedule
# import time 

# # Timeout es para que se detenga luego de 5 minutos (60 segudos multiplicado por 5)
# timeout = time.time() + 60*5

# schedule.every(30).seconds.do(insert_simbolos, valores)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

#     if time.time() > timeout:
#         break