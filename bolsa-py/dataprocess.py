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

def selectLastValues(tablaMySQL, limit):

    #instanciamos bases de datos
    db = Database(config)
        
    queryGetTitulos = "SELECT * FROM `"+str(tablaMySQL)+""
    
    titulos = db.run_query(queryGetTitulos)
    
    return titulos

#recorre las distintas bases de datos locales para insertarlo en las distintas colecciones en firestore
def insertLastSimbolsValuesInFirebase():
    paneles = config.paneles
    fb = Firestore(config)

    for panel in paneles:


        titulos = selectLastValues(panel['mysql'], panel['default_limit'])

        newdoc = {
            "name_panel" : panel['name'],
            "date": time.strftime('%Y-%m-%d %H:%M:%S'),
            "titulos" : []
        }

        for titulo in titulos:
            newTitulo = {
                "simbolo": titulo['simbolo'],
                "puntas" : {
                    "cantidadCompra" : str( titulo['puntas_cantidad_compra'] ),
                    "precioCompra" : str( titulo['puntas_precio_compra'] ),
                    "precioVenta" : str( titulo['puntas_precio_venta'] ),
                    "cantidadVenta" : str( titulo['puntas_cantidad_venta'] ),
                },
                "ultimoPrecio" : str( titulo['ultimo_precio'] ),
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

        #1 recuperamos los simbols en caso de que haya alguno
        queryGetSimbols = "SELECT * FROM `options` WHERE name='"+str(panel['mysql'])+"'"
        resp = db.run_query(queryGetSimbols)
        
        if resp is None:
            query = "UPDATE options SET value = '"+simbolos+"' WHERE name ='"+str(panel['mysql'])+"'"
        else:
            query = "INSERT INTO `options` (`name`, `value` ) VALUES ('"+str(panel['mysql'])+"', '"+simbolos+"')"
        
        mysqlResp = db.run_query(query)

        print(mysqlResp)

