import os
import config
from db import Database
import json

#valores = "'ALUA', '80.0', '48.700', '49.800', '200.0', '49.500', '0.81', '49.000', '49.600', '48.200', '49.500', '427110.0', '812.0', '2020-09-08T17:00:04.807', NULL, NULL, NULL, 'BCBA', 'AR$'"

db = Database(config)

with open(config.basedir+"/valores.json") as json_file:
    data = json.load(json_file)
    print(data['titulos'][0]['fecha'] )

    for simbolo in data['titulos']:
        #le pongo las doble comillas porque todo es texto y la comilla single para que mysql entienda que es una variable, si es null, va SIN comillas simples pero siempre dentro de las dos comillas
        # simb = "'"+simbolo['simbolo']+"'"
        # pCantCompra = "'"+simbolo['puntas']['cantidadCompra']+"'"
        # pPreCompra= "'"+simbolo['puntas']['precioCompra']+"'"
        # pPreVenta = "'"+simbolo['puntas']['precioVenta']+"'"
        # pCantVenta= "'"+simbolo['puntas']['cantidadVenta']+"'"
        # ultPrecio= "'"+simbolo['ultimoPrecio']+"'"
        # varPorcent = "'"+simbolo['variacionPorcentual']+"'"
        # apert = "'"+simbolo['apertura']+"'"
        # maximo = "'"+simbolo['maximo']+"'"
        # minimo = "'"+simbolo['minimo']+"'"
        # ultCierre = "'"+simbolo['ultimoCierre']+"'"
        # volumen = "'"+simbolo['volumen']+"'"
        # cantOper =  "'"+simbolo['cantidadOperaciones']+"'"
        # fecha = "'"+simbolo['fecha']+"'"
        # tipoOpc = "NULL" if simbolo['tipoOpcion'] == 'null' else "'"+simbolo['tipoOpcion']+"'"
        # precEjerc = "NULL" if simbolo['precioEjercicio'] == 'null' else "'"+simbolo['precioEjercicio']+"'"
        # fechaVenc= "NULL" if simbolo['fechaVencimiento'] == 'null' else "'"+simbolo['fechaVencimiento']+"'"
        # mercado = "'"+simbolo['mercado']+"'"
        # moneda = "'"+simbolo['moneda']+"'"

        # valores = simb + ", " + pCantCompra + ", " + pPreCompra + ", " + pPreVenta + ", " + pCantVenta + ", " + ultPrecio + ", " +varPorcent + ", " + apert + ", " + maximo + ", " + minimo + ", " + ultCierre + ", " + volumen + ", " + cantOper + ", " + fecha + ", " + tipoOpc + ", " + precEjerc + ", " + fechaVenc + ", " + mercado + ", " + moneda

        valores = [
            (simbolo['simbolo'], simbolo['puntas']['cantidadCompra'], simbolo['puntas']['precioCompra'], simbolo['puntas']['precioVenta'], simbolo['puntas']['cantidadVenta'], simbolo['ultimoPrecio'], simbolo['variacionPorcentual'], simbolo['apertura'], simbolo['maximo'], simbolo['minimo'], simbolo['ultimoCierre'], simbolo['volumen'], simbolo['cantidadOperaciones'], simbolo['fecha'], simbolo['tipoOpcion'], simbolo['precioEjercicio'], simbolo['fechaVencimiento'], simbolo['mercado'], simbolo['moneda'])
        ]
        
        
        

        queryResponse = db.insert_valores_simbolo(valores)

        break
        
        

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