import urllib.request
import urllib.parse
import json

class ApiInvertirOnline:
    """Database connection class."""

    def __init__(self):
        self.urlBase = 'https://api.invertironline.com/api/v2/'    


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
            respuesta['data'] = response.read()
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
    def getToken(self, refresh_token=False, user="", password=""):
        respuesta = {}
        respuesta['status'] = {}
        
        url = 'https://api.invertironline.com/token'

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
            "Content-Type" : "application/x-www-form-urlencoded"
        }

        if refresh_token == False :         
            valores = {
                "grant_type" : "password",
                "username" : user,
                "password" : password
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

        req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
        
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
    def getCotizacionesAcciones(self, token):
        
        panel = 'Merval'
        instrumento = 'acciones'
        pais = 'argentina'

        url = 'Cotizaciones/Acciones/Merval/Argentina?panelCotizacion.instrumento='+instrumento+'&panelCotizacion.panel='+panel+'&panelCotizacion.pais='+pais
                
        return self.getFectchDataByGet(token, url)





# invOnlFetchToekn = ApiInvertirOnline()
# resp = invOnlFetchToekn.getToken(False, 'cocodelacueva', 'EmiliaIsabela44')
# print(resp['data']['access_token'])

#jsonRespuesta = {"access_token":"fulTECkpVCQc9MXkFitGEhtHbDqFjvgAJ-E2u0bP43Rp2BlBhuaJx0aM20EIfHXJyLUP1PiyrHZzfyckJzyHdPNN6tt3DqkdcQ-C17cx96-E4Gp4pT9Et-ULCHYQkOJ5egZhG_QaFpOHXIVYKU8spkmWu8KLFtJ-452aksok152XUlc0bZBGap9lMFwJjs2z90I8JynbRNZs38q1RoBtqAbHwFYeYTEWg9RZnQK9bg3p9Z1_HlRM9hr6ud3IEc4yaKp5Y270oIyar4FOtmM6TR2UHp7Qkzap6UWaAZ5vwamGBjHUH--UGzAJ5Uvdw5AxU6i_Pdk9Px4co8Lg64Nra7pZaI2Dvmc2cH2ZHXQ4e0vy6xb7OedCAN3kg5Yi2_v2","token_type":"bearer","expires_in":899,"refresh_token":"wxgBEg4HqFDiE62YenhjIMnU6qr5-vK4YMiDuFN17O3LexBRhoJ79ZQ9lAbYKa1NdI_WgA_FnWh5QjlnNSV6fwrDBAHO55oexgk6Oq8XMOshNQRbIVfHkG7E8LeExfd0wI1JYriztBNa-yze_r0eDZMyfKTGXF2oV9QQglCV6OEFp33S_HxKRAY0b1F7_8yI1KFWCqnYYzZUSh6ru2O2_BaZqHETHid_BdE940mbuXxIwculS1ZyYt_W4bfH4X7pN8ClvqUVCSbd9gs3wIZa9wMnFm7XRrPPlSdp05h9EqSLGnyoZLb1nFp7YA1XRB8UhfSwggnrq2ZSfNoy2FYeHAXBkFuiFVXaGkmABvNDgqY9VQmEhRzfSBC5BVuZscig",".issued":"Thu, 17 Sep 2020 01:01:54 GMT",".expires":"Thu, 17 Sep 2020 01:16:54 GMT",".refreshexpires":"Thu, 17 Sep 2020 02:01:54 GMT"}

#datos = ApiInvertirOnline()



#data = json.load(jsonRespuesta)
#print(data)
#resp = datos.getToken(False, 'cocodelacueva', 'EmiliaIsabela44')
#resp = datos.getToken(token)
# resp = datos.getCotizacionesAcciones(data['access_token'])
# print(resp['data'])
