import urllib.request
import urllib.parse
import json


#clase que hace los pedidos fetch a la base de invertir online
class ApiInvertirOnline:
    """Database connection class."""

    def __init__(self, config):
        self.urlBase = config.urlApilBase
        self.urlToken = config.urlApiToken
        self.apiUsername = config.apiUser
        self.apiPassword = config.apiPw


    #Toma la data por get
    def getFectchDataByGet(self, token, url):

        respuesta = {}
        respuesta['status'] = {}

        urlFetch = self.urlBase + url

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
            "Authorization" : "Bearer "+token 
        }

        req = urllib.request.Request(url=urlFetch, headers=headers)
        
        try:
            response = urllib.request.urlopen(req)
            respuesta['status']['code'] = 200
            respuesta['status']['error'] = False
            respuesta['data'] = json.loads(response.read().decode('ascii'))
            response.close()

        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                print('Error Code: ', e.code)
                respuesta['status']['code'] = 'token-error'
                respuesta['status']['error'] = e.code
           
            elif hasattr(e, 'reason'):
                print("Reason code: ", e.reason)
                respuesta['status']['error'] = e.reason
        
        return respuesta


    #para pedidos por post, recibe los valores entre un objeto {} y la url hasta la ?
    def getFectchDataByPOST(self, token, url, values):

        respuesta = {}
        respuesta['status'] = {}
        urlFetch = self.urlBase + url

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
            "Authorization" : "Bearer "+token 
        }

        req = urllib.request.Request(urlFetch, values, headers)
        
        try:
            response = urllib.request.urlopen(req)
            respuesta['status']['code'] = 200
            respuesta['status']['error'] = False
            respuesta['data'] = json.loads(response.read().decode('ascii'))
            response.close()

        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                print('Error Code: ', e.code)
                respuesta['status']['code'] = 'token-error'
           
            elif hasattr(e, 'reason'):
                print("Reason code: ", e.reason)
                respuesta['status']['error'] = e.reason
        
        return respuesta


    #login, primer token
    def getToken(self, refresh_token=False):
        respuesta = {}
        respuesta['status'] = {}

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
            "Content-Type" : "application/x-www-form-urlencoded"
        }

        if refresh_token == False :         
            valores = {
                "grant_type" : "password",
                "username" : self.apiUsername,
                "password" : self.apiPassword
            }
            data = urllib.parse.urlencode(valores)
            data = data.encode('ascii')
            
        else :
            valores = {
                "grant_type" : "refresh_token",
                "refresh_token" : refresh_token
            }
            data = urllib.parse.urlencode(valores)
            data = data.encode('ascii')

        req = urllib.request.Request(url=self.urlToken, data=data, headers=headers, method="POST")
        
        try:
            response = urllib.request.urlopen(req)
            respuesta['status']['code'] = 200
            respuesta['status']['error'] = False
            respuesta['data'] = json.loads(response.read().decode('ascii'))
            response.close()

        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                print('Error Code: ', e.code)
                respuesta['status']['code'] = 'token-error'
           
            elif hasattr(e, 'reason'):
                print("Reason code: ", e.reason)
                respuesta['status']['error'] = e.reason
        
        return respuesta

    #funcion standard que pide las cotizaciones
    def getCotizacionesAcciones(self, token, panel):
        
        instrumento = 'acciones'
        pais = 'argentina'

        url = 'Cotizaciones/'+instrumento+'/'+panel+'/'+pais+'?panelCotizacion.instrumento='+instrumento+'&panelCotizacion.panel='+panel+'&panelCotizacion.pais='+pais
                
        return self.getFectchDataByGet(token, url)


    #esta funcion arma por completo el siclo que se hace cada 50 minutos, pide los token pide las cotizaciones, guarda en la bd
    def cicleTokenValoresOnApi(self, refToken, panel):
        respuesta = {}
        respuesta['status'] = {}
        respuesta['status']['code'] = 'ok'
        respuesta['status']['error'] = False

        #primer intento con refToken
        resp1 = self.getToken(refToken)
        if resp1['status']['code'] == 200:

            token = resp1['data']['access_token']
            respuesta['newrefToken'] = resp1['data']['refresh_token']
            
            #va a buscar cotizaciones
            resp2 = self.getCotizacionesAcciones(token, panel)
            if resp2['status']['code'] == 200:
                
                respuesta['data'] = resp2['data']

            else : 
                print('falla refreshToken')
                
                respuesta['status']['code'] = 'error-get-valores'
                respuesta['status']['error'] = resp2['status']['code']

        #sedundo intento
        #si el refresh token falla va a buscar el primer token con user y pw
        else : 
            print('falla refreshToken')
            
            resp2 = self.getToken(False)
            if resp2['status']['code'] == 200:

                token = resp2['data']['access_token']
                respuesta['newrefToken'] = resp2['data']['refresh_token']
                
                #va a buscar cotizaciones
                resp3 = self.getCotizacionesAcciones(token, panel)
                if resp3['status']['code'] == 200:
                    
                    respuesta['data'] = resp3['data']

                else : 
                    print('falla get Valores')
                    
                    respuesta['status']['code'] = 'error-get-valores'
                    respuesta['status']['error'] = resp3['status']['code']


            else : 
                print('falla Token')
                respuesta['status']['code'] = 'error-token'
                respuesta['status']['error'] = resp2['status']['code']


        #finalmente, pase lo que pase, devuelve la respuesta con la info
        return respuesta


#clase que hace los pedidos fetch a la api de dolar si
class ApiDolarSi:

    """Database connection class."""

    def __init__(self):
        self.urlBase = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'


    #Toma la data por get
    def getFectchDataByGet(self):

        respuesta = {}
        respuesta['status'] = {}

        urlFetch = self.urlBase

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
        }

        req = urllib.request.Request(url=urlFetch, headers=headers)
        
        try:
            response = urllib.request.urlopen(req)
            respuesta['status']['code'] = 'ok'
            respuesta['status']['error'] = False
            respuesta['data'] = json.loads(response.read().decode('ascii'))
            response.close()

        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                print('Error Code: ', e.code)
                respuesta['status']['code'] = 'api-dolar-error'
                respuesta['status']['error'] = e.code
           
            elif hasattr(e, 'reason'):
                print("Reason code: ", e.reason)
                respuesta['status']['error'] = e.reason
        
        return respuesta

#clase que hace los pedidos fetch a la api de qubit broker, que no es una api en sí, pero me sirve la data
class ApiQubitBroker:

    """Database connection class."""

    def __init__(self):
        self.urlBase = 'https://www.qubit.com.ar/c_value'


    #Toma la data por get
    def getFectchDataByGet(self):

        respuesta = {}
        respuesta['status'] = {}

        urlFetch = self.urlBase

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
        }

        req = urllib.request.Request(url=urlFetch, headers=headers)
        
        try:
            response = urllib.request.urlopen(req)
            respuesta['status']['code'] = 'ok'
            respuesta['status']['error'] = False
            respuesta['data'] = json.loads(response.read().decode('ascii'))
            response.close()

        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                print('Error Code: ', e.code)
                respuesta['status']['code'] = 'api-qubit-error'
                respuesta['status']['error'] = e.code
           
            elif hasattr(e, 'reason'):
                print("Reason code: ", e.reason)
                respuesta['status']['error'] = e.reason
        
        return respuesta