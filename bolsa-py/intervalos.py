import os
import config
import time 
from db import Database
from fetch import ApiInvertirOnline, ApiDolarSi
import decimal

#mediante la api de invertir online hace un pedido y trae los paneles definidos y los guarda en mysql
def insertSimbolosInDB():

    # VARIABLES VASICAS
    refresToken = False #refresh token por defecto en falso
    datosFetch = [
        {
            "panel" : 'Panel%20General',
            "tabla":  'panel_general'
        },
        {
            "panel" : 'CEDEARs',
            "tabla":  'panel_cedears'
        }
    ]



    #se instancian las clases
    invOnlFetch = ApiInvertirOnline(config)
    db = Database(config)


    #1 recuperamos el refresh token de la bd
    queryGetToken = "SELECT * FROM `options` WHERE name='refresh-token'"
    
    
    for x in datosFetch:
        
        respToken = db.run_query(queryGetToken)
        if respToken[0]['value'] != '':
            refresToken = respToken[0]['value']


        respuesta = invOnlFetch.cicleTokenValoresOnApi(refresToken, x["panel"])

        #si repsuesta es ok, se graba en la bd los valores y el newRefrestoken
        if respuesta['status']['code'] == 'ok':
            valores = []  
            data = respuesta['data']
           
            for simbolo in data['titulos']:
                
                if ( simbolo['puntas'] != None ):
                    valor = (simbolo['simbolo'], simbolo['puntas']['cantidadCompra'], simbolo['puntas']['precioCompra'], simbolo['puntas']['precioVenta'], simbolo['puntas']['cantidadVenta'], simbolo['ultimoPrecio'], simbolo['variacionPorcentual'], simbolo['apertura'], simbolo['maximo'], simbolo['minimo'], simbolo['ultimoCierre'], simbolo['volumen'], simbolo['cantidadOperaciones'], simbolo['fecha'], simbolo['tipoOpcion'], simbolo['precioEjercicio'], simbolo['fechaVencimiento'], simbolo['mercado'], simbolo['moneda'])
                else :
                    valor = (simbolo['simbolo'], 0, 0, 0, 0, simbolo['ultimoPrecio'], simbolo['variacionPorcentual'], simbolo['apertura'], simbolo['maximo'], simbolo['minimo'], simbolo['ultimoCierre'], simbolo['volumen'], simbolo['cantidadOperaciones'], simbolo['fecha'], simbolo['tipoOpcion'], simbolo['precioEjercicio'], simbolo['fechaVencimiento'], simbolo['mercado'], simbolo['moneda'])
                
                
                valores.append(valor)
    
            queryResponse = db.insert_valores_simbolo(x["tabla"], valores)
            print(queryResponse)

            #guarda el refresh token
            newRefresToken = respuesta['newrefToken']
            if newRefresToken != '':
                query = "UPDATE options SET value = '"+newRefresToken+"' WHERE name = 'refresh-token'"
                db.run_query(query)

                error = 'ok'
                extraData = 'valores-recuperados-'+x["panel"]
                query = "INSERT INTO `logs` (`error_code`, `extra-data` ) VALUES ('"+error+"', '"+extraData+"')"
                db.run_query(query)

        else :
            error = 'error-'+x["panel"]
            extraData = respuesta['status']['code']
            query = "INSERT INTO `logs` (`error_code`, `extra-data` ) VALUES ('"+error+"', '"+extraData+"')"
            db.run_query(query)


    print('ciclo terminado')


#mediante la api de dolar si  hace un pedido y trae los valores y los guarda en mysql
def insertDolaresInDB():
    dolarFetch = ApiDolarSi()
    db = Database(config)
    valores_dolar = dolarFetch.getFectchDataByGet()
    
    if valores_dolar['status']['code'] == 'ok':
        valores = []  

        for casa in valores_dolar['data']:
            valor = casa['casa']
            #valor['agencia']
            #valor['compra']
            #valor['decimales']
            #valor['nombre']
            #valor['variacion']
            #valor['venta']
            #valor['ventaCero']
            if (valor['nombre'] == 'Dolar Oficial') :
                slug = 'dolar-oficial'
            elif (valor['nombre'] == 'Dolar Blue' ) : 
                slug = 'dolar-blue'
            elif (valor['nombre'] == 'Dolar Contado con Liqui' ) : 
                slug = 'dolar-contado-liqui'
            elif (valor['nombre'] == 'Dolar Bolsa' ) : 
                slug = 'dolar-bolsa'
            elif (valor['nombre'] == 'Dolar turista' ) : 
                slug = 'dolar-turista'
            else :
                continue
            
            if valor['compra'] != 'No Cotiza' :
                compra = valor['compra'].split(',')
                compra = compra[0] + '.' + compra[1]
                compra = decimal.Decimal(compra)
            else :
                compra = None
            if valor['venta'] != 'No Cotiza' :
                venta = valor['venta'].split(',')
                venta = venta[0] + '.' + venta[1]
                venta = decimal.Decimal(venta)
            else :
                venta = None

            valor = (valor['nombre'], slug, compra, venta)
                
            valores.append(valor)
    
        queryResponse = db.insert_dolares('cotizacion_dolares', valores)
        print(queryResponse)

        #guarda log
        error = 'ok'
        extraData = 'dolares-actualizados'
        query = "INSERT INTO `logs` (`error_code`, `extra-data` ) VALUES ('"+error+"', '"+extraData+"')"
        db.run_query(query)
    
    else :
        error = 'error-dolares'
        extraData = str(valores_dolar['status']['code'])
        query = "INSERT INTO `logs` (`error_code`, `extra-data` ) VALUES ('"+error+"', '"+extraData+"')"
        db.run_query(query)

    return 'Cotización dolares actualizada'

    
    
