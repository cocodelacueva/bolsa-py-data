import os
import config
#from db import Database
import json
from fetch import ApiInvertirOnline
valores = []
token = ''
refresToken = False



#pide el token por primera vez y pide cotizaciones
def getFirstToken(us, pw):
    invOnlFetchToekn = ApiInvertirOnline()
    resp = invOnlFetchToekn.getToken(False, us, pw)
    if resp['status']['code'] == 200:
        global token
        global refreshToken
        token = resp['data']['access_token']
        refresToken = resp['data']['refresh_token']

        getCotizaciones(token)

    else : 
        print('falla getToken')
        print(resp['status']['code'])
        print(resp['status']['error'])
        return


#toma el frefresh token para buscar un token y pedir cotizaciones
def refreshToken(refToken):
    
    invOnlFetchToekn = ApiInvertirOnline()
    resp = invOnlFetchToekn.getToken(refToken)
    if resp['status']['code'] == 200:
        global token
        global refreshToken
        token = resp['data']['access_token']
        refresToken = resp['data']['refresh_token']

        getCotizaciones(token)

    else : 
        print('falla refreshToken')
        
        getFirstToken(user, password)

        return


# pide las cotizaciones de los titulos
def getCotizaciones(token):
    
    invOnlFetchToekn = ApiInvertirOnline()
    resp = invOnlFetchToekn.getCotizacionesAcciones(token)

    if resp['status']['code'] == 200:
        
        data = resp['data']
        print(data)
        for simbolo in data['titulos']:

            valor = (simbolo['simbolo'], simbolo['puntas']['cantidadCompra'], simbolo['puntas']['precioCompra'], simbolo['puntas']['precioVenta'], simbolo['puntas']['cantidadVenta'], simbolo['ultimoPrecio'], simbolo['variacionPorcentual'], simbolo['apertura'], simbolo['maximo'], simbolo['minimo'], simbolo['ultimoCierre'], simbolo['volumen'], simbolo['cantidadOperaciones'], simbolo['fecha'], simbolo['tipoOpcion'], simbolo['precioEjercicio'], simbolo['fechaVencimiento'], simbolo['mercado'], simbolo['moneda'])

            valores.append(valor)
        
        print(valores)
        #db = Database(config)
        #queryResponse = db.insert_valores_simbolo(valores)

    else : 
        print('falla getValores')
        print(resp['status']['code'])
        print(resp['status']['error'])
        return

        
# accede a la api de invertir online para acceder a los datos

if refresToken == False:
    
    getFirstToken(user, password)

else:
    refreshToken(refreshToken)
