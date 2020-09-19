import os
import config
import schedule
import time 
from db import Database
from fetch import ApiInvertirOnline


def insert_simbolos_in_db():

    valores = [] #los valores que se van a grabar luego
    refresToken = False #refresh token por defecto en falso

    #se instancian las clases
    invOnlFetch = ApiInvertirOnline(config)
    db = Database(config)


    #1 recuperamos el refresh token de la bd
    querySelect = "SELECT * FROM `options` WHERE name='refresh-token'"
    resp = db.run_query(querySelect)
    if resp[0][2] != '':
        refresToken = resp[0][2]

    #con el refresh token hacemos el pedido (primero va a buscar el token)
    respuesta = invOnlFetch.cicleTokenValoresOnApi(refresToken)

    #si repsuesta es ok, se graba en la bd los valores y el newRefrestoken
    if respuesta['status']['code'] == 'ok':
            
        data = respuesta['data']
        
        for simbolo in data['titulos']:

            valor = (simbolo['simbolo'], simbolo['puntas']['cantidadCompra'], simbolo['puntas']['precioCompra'], simbolo['puntas']['precioVenta'], simbolo['puntas']['cantidadVenta'], simbolo['ultimoPrecio'], simbolo['variacionPorcentual'], simbolo['apertura'], simbolo['maximo'], simbolo['minimo'], simbolo['ultimoCierre'], simbolo['volumen'], simbolo['cantidadOperaciones'], simbolo['fecha'], simbolo['tipoOpcion'], simbolo['precioEjercicio'], simbolo['fechaVencimiento'], simbolo['mercado'], simbolo['moneda'])

            valores.append(valor)

    
        queryResponse = db.insert_valores_simbolo(valores)
        print(queryResponse)

        #guarda el refresh token
        newRefresToken = respuesta['newrefToken']
        if newRefresToken != '':
            query = "UPDATE options SET value = '"+newRefresToken+"' WHERE name = 'refresh-token'"
            db.run_query(query)

            error = 'ok'
            extraData = 'valores-recuperados'
            query = "INSERT INTO `logs` (`error_code`, `extra-data` ) VALUES ('"+error+"', '"+extraData+"')"
            db.run_query(query)

    else :
        error = 'error'
        extraData = respuesta['status']['code']
        query = "INSERT INTO `logs` (`error_code`, `extra-data` ) VALUES ('"+error+"', '"+extraData+"')"
        db.run_query(query)

    print('ciclo terminado')



# Actividad repetitiva:
def intervaloUpdatingMerval():

    # Timeout es para que se detenga luego de 8 horas (60 segudos multiplicado por 60 MINUTOS MULTIPLICADO POR 8)
    timeout = time.time() + 60*60*7

    schedule.every(config.minutesInterval).minutes.do(insert_simbolos_in_db)

    while True:
        schedule.run_pending()
        time.sleep(1)

        if time.time() > timeout:
            break
