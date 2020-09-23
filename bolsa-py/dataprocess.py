import os
import config
import time 
from db import Database
from firebase import Firestore


#selecciona las acciones del dia anterior, o del actual de acuerdo al prev pasado
def select1DayBefore(tablaMySQL, prev='0'):

    #instanciamos bases de datos
    db = Database(config)
        
    queryGetTitulos = "SELECT * FROM `"+str(tablaMySQL)+"` WHERE date(time_stamp)=(CURDATE()-"+str(prev)+")"
    
    titulos = db.run_query(queryGetTitulos)
    
    return titulos


#recorre las distintas bases de datos locales para insertarlo en las distintas colecciones en firestore
def getDataFromDBinsertinFirebase(paneles, dia):

    fb = Firestore(config)

    for panel in paneles:


        titulos = select1DayBefore(panel['mysql'],dia)

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

