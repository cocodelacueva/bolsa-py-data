import os
import config
import time 
from db import Database
from firebase import Firestore
import decimal


#selecciona las acciones del dia anterior, o del actual de acuerdo al prev pasado
def selectValuesToday(tablaMySQL):

    #instanciamos bases de datos
    db = Database(config)
        
    queryGetTitulos = "SELECT * FROM `"+str(tablaMySQL)+"` WHERE date(time_stamp)=CURDATE()"
    
    titulos = db.run_query(queryGetTitulos)
    
    return titulos

# selecciona los ultimos valores con el limite pasado, puede ser 1 o 500
def selectLastValues(tablaMySQL, limit):

    #instanciamos bases de datos
    db = Database(config)
        
    queryGetTitulos = "SELECT * FROM `"+str(tablaMySQL)+" LIMIT " + limit + " ORDER BY time_stamp DESC"
    
    titulos = db.run_query(queryGetTitulos)
    
    return titulos


#selecciona las acciones del dia anterior, o del actual de acuerdo al prev pasado
def selectTituloBySimbolInPanel(tablaMySQL, simbol, orden=None, limit=None):

    #instanciamos bases de datos
    db = Database(config)
        
    query = "SELECT * FROM `"+str(tablaMySQL)+"` WHERE simbolo='"+simbol+"'"

    if orden != None:
        query += " " + str(orden)

    if limit != None:
        query += " LIMIT " + str(limit)
    
    titulo = db.run_query(query)
    
    return titulo

#recorre las distintas bases de datos locales para insertarlo en las distintas colecciones en firestore
def insertLastSimbolsValuesInFirebase():
    paneles = config.paneles
    db = Database(config)
    fb = Firestore(config)

    for panel in paneles:

        #primero toma los simbolos
        queryGetSimbols = "SELECT * FROM `options` WHERE name='simbolos_"+str(panel['mysql'])+"'"
        simbolos = db.run_query(queryGetSimbols)
        
        if simbolos is None:
            getSimbolosNames()
            return

        #separamos el string para convertilo en lista y recorre cada valor
        simbolos = simbolos[0]['value'].split('/')


        #armamos el documento nuevo para guardar en firebase
        newdoc = {
            "name_panel" : panel['name'],
            "date": time.strftime('%Y-%m-%d %H:%M:%S'),
            "titulos" : []
        }

        #recorre cada simbolo para buscar su valor
        for simbolo in simbolos:
            titulos = selectTituloBySimbolInPanel(panel['mysql'], simbolo, 'ORDER BY time_stamp DESC', 1)
            titulo = titulos[0]

            #calculamos la variacion y la tendencia:

            diferencia = titulo['ultimo_precio'] - titulo['ultimo_cierre']
            
            if diferencia > 0:
                tendencia = "sube"
                dif = decimal.Decimal( ( (( titulo['ultimo_precio'] - titulo['ultimo_cierre'] ) / titulo['ultimo_cierre']) * 100) )
                s = '{:0.2f}'.format(dif)
                variacionDiaria = str( s + '%')

            elif diferencia < 0:
                tendencia = "baja"
                dif = decimal.Decimal( (( titulo['ultimo_cierre'] - titulo['ultimo_precio'] ) / titulo['ultimo_precio']) * 100)
                s = '{:0.2f}'.format(dif)
                variacionDiaria = str('-' + s + '%')

            else:
                tendencia = "estable"
                variacionDiaria = str('0%')

            titulo['ultimo_cierre']

            newTitulo = {
                "simbolo": titulo['simbolo'],
                "puntas" : {
                    "cantidadCompra" : str( titulo['puntas_cantidad_compra'] ),
                    "precioCompra" : str( titulo['puntas_precio_compra'] ),
                    "precioVenta" : str( titulo['puntas_precio_venta'] ),
                    "cantidadVenta" : str( titulo['puntas_cantidad_venta'] ),
                },
                "ultimoPrecio" : str( titulo['ultimo_precio'] ),
                "tendencia" : str(tendencia),
                "variacionPorcentual": str( titulo['variacion_porcentual'] ),
                "apertura" : str( titulo['apertura'] ),
                "maximo" : str( titulo['maximo'] ),
                "minimo" : str( titulo['minimo'] ),
                "ultimoCierre" : str( titulo['ultimo_cierre'] ),
                "volumen" : str( titulo['volumen'] ),
                "cantidadOperaciones" : str( titulo['cantidad_operaciones'] ),
                "fechaData" : titulo['fecha'],
                "tipoOpcion": titulo['tipo_opcion'],
                "precioEjercicio" : str( titulo['precio_ejercicio'] ),
                "fechaVencimiento" : titulo['fecha_vencimiento'],
                "mercado" : titulo['mercado'],
                "moneda" : titulo['moneda'],
                "variacionDiaria": variacionDiaria,
            }

            newdoc["titulos"].append(newTitulo)

        saveFS = fb.updateDocinCollection('cotizaciones', panel['firestore'], newdoc)
        print(saveFS)
        
        error = 'ok'
        extraData = 'firebase-actualizada-'+panel["mysql"]
        query = "INSERT INTO `logs` (`error_code`, `extra-data` ) VALUES ('"+error+"', '"+extraData+"')"
        rlog = db.run_query(query)
        print(rlog)



#actualiza el string de simbolos que sirve para actualizar firebase: insertLastSimbolsValuesInFirebase()
def getSimbolosNames():
    paneles = config.paneles
    db = Database(config)

    for panel in paneles:
        
        query = "SELECT * FROM `"+str(panel['mysql'])+"` LIMIT " + str(panel['default_limit'])
        
        titulos = db.run_query(query)
        simbolos = []

        for titulo in titulos:
            if titulo['simbolo'] not in simbolos:
                simbolos.append(titulo['simbolo'])
            

        simbolos = '/'.join(simbolos)
        fecha = time.strftime('%Y-%m-%d')

        query = "UPDATE options SET value = '"+simbolos+"', extra_value='"+fecha+"' WHERE name ='simbolos_"+str(panel['mysql'])+"'"
        
        mysqlResp = db.run_query(query)

        print(mysqlResp)

        error = 'ok'
        extraData = 'simbolos-actualizados-'+panel["mysql"]
        query = "INSERT INTO `logs` (`error_code`, `extra-data` ) VALUES ('"+error+"', '"+extraData+"')"
        rlog = db.run_query(query)

        print(rlog)


#inserta los ultimos valores de dolares en firebase
def insertLastDolarsValuesInFirebase():
    dolaresConfig = config.dolares
    db = Database(config)
    fb = Firestore(config)

    nuevoDocumento = {
        "date": time.strftime('%Y-%m-%d %H:%M:%S'),
        "valores" : []
    }

    query = "SELECT * FROM `"+str(dolaresConfig['mysql'])+"` WHERE date(timestamp)=CURDATE() LIMIT "+str(dolaresConfig['default_limit'])
        
    cotizaciones = db.run_query(query)
    
    if cotizaciones:
        for cot in cotizaciones:
            valor = {}

            valor['nombre'] = str(cot['nombre'])
            valor['slug'] = str(cot['slug'])
            valor['compra'] = str(cot['compra'])
            valor['venta'] = str(cot['venta'])
            
            nuevoDocumento['valores'].append(valor)

        saveFS = fb.updateDocinCollection('cotizaciones', dolaresConfig['firestore'], nuevoDocumento)
        print(saveFS)


#inserta los ultimos valores de monedas digitales en firebase
def insertLastDigitalCoinsValuesInFirebase():
    dcoinsConfig = config.monedasDigitales
    db = Database(config)
    fb = Firestore(config)

    nuevoDocumento = {
        "date": time.strftime('%Y-%m-%d %H:%M:%S'),
        "valores" : []
    }

    query = "SELECT * FROM `"+str(dcoinsConfig['mysql'])+"` WHERE date(timestamp)=(CURDATE()-1) ORDER BY id DESC LIMIT "+str(dcoinsConfig['default_limit'])

    cotizaciones = db.run_query(query)
    
    if cotizaciones:
        
        for cot in cotizaciones:
            valor = {}

            valor['simbol'] = str(cot['simbol'])
            valor['valorDolar'] = str(cot['valor_dolar'])
            valor['valorPesos'] = str(cot['valor_pesos'])
            
            nuevoDocumento['valores'].append(valor)

        saveFS = fb.updateDocinCollection('cotizaciones', dcoinsConfig['firestore'], nuevoDocumento)
        print(saveFS)