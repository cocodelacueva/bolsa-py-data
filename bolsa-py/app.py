import os
import config
from db import Database
import json

#valores = "'ALUA', '80.0', '48.700', '49.800', '200.0', '49.500', '0.81', '49.000', '49.600', '48.200', '49.500', '427110.0', '812.0', '2020-09-08T17:00:04.807', NULL, NULL, NULL, 'BCBA', 'AR$'"

db = Database(config)

with open(config.basedir+"/valores.json") as json_file:
    data = json.load(json_file)
    print(data['titulos'][0]['fecha'] )
    valores = []

    for simbolo in data['titulos']:

        valor = (simbolo['simbolo'], simbolo['puntas']['cantidadCompra'], simbolo['puntas']['precioCompra'], simbolo['puntas']['precioVenta'], simbolo['puntas']['cantidadVenta'], simbolo['ultimoPrecio'], simbolo['variacionPorcentual'], simbolo['apertura'], simbolo['maximo'], simbolo['minimo'], simbolo['ultimoCierre'], simbolo['volumen'], simbolo['cantidadOperaciones'], simbolo['fecha'], simbolo['tipoOpcion'], simbolo['precioEjercicio'], simbolo['fechaVencimiento'], simbolo['mercado'], simbolo['moneda'])

        valores.append(valor)
        
    queryResponse = db.insert_valores_simbolo(valores)
        

# db = Database(config)
# queryResponse = db.insert_valores_simbolo(valores)
# print(queryResponse)





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