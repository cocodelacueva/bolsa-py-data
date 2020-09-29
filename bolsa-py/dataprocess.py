import os
import config
import time 
from db import Database
from firebase import Firestore


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
def selectTituloBySimbolInPanel(tablaMySQL, simbol, limit=None):

    #instanciamos bases de datos
    db = Database(config)
        
    query = "SELECT * FROM `"+str(tablaMySQL)+"` WHERE simbolo='"+simbol+"'"

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
        queryGetSimbols = "SELECT * FROM `options` WHERE name='"+str(panel['mysql'])+"'"
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
            titulos = selectTituloBySimbolInPanel(panel['mysql'], simbolo, 2)
            diferencia = titulos[1]['ultimo_precio'] - titulos[0]['ultimo_precio']
            if diferencia > 0:
                tendencia = "sube"
            elif diferencia < 0:
                tendencia = "baja"
            else:
                tendencia = "estable"

            titulo = titulos[1]

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
                "moneda" : titulo['moneda']
            }

            newdoc["titulos"].append(newTitulo)

        saveFS = fb.addDoc(newdoc, panel['firestore'])
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

        #1 recuperamos los simbols en caso de que haya alguno
        queryGetSimbols = "SELECT * FROM `options` WHERE name='"+str(panel['mysql'])+"'"
        resp = db.run_query(queryGetSimbols)
        
        if resp is None:
            query = "UPDATE options SET value = '"+simbolos+"', extra_value='"+fecha+"' WHERE name ='"+str(panel['mysql'])+"'"
        else:
            query = "INSERT INTO `options` (`name`, `value`, `extra_value`) VALUES ('"+str(panel['mysql'])+"', '"+simbolos+"', '"+fecha+"')"
        
        mysqlResp = db.run_query(query)

        print(mysqlResp)

        error = 'ok'
        extraData = 'simbolos-actualizados-'+panel["mysql"]
        query = "INSERT INTO `logs` (`error_code`, `extra-data` ) VALUES ('"+error+"', '"+extraData+"')"
        rlog = db.run_query(query)

        print(rlog)

