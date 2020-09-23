# Bolsa py data

Captura los datos de valores de la bolsa para volcarlos en algunas bases de datos.

## Datos api
* Invertir online (tiene un limite de llamadas por día)

## Bases de datos

* MySQL: Guarda los datos duros para analizarlos luego y volcarlos a la base de datos online.
* Firebase: Datos online, estos datos se consumen desde el front end.

## CODIGO

Armado en python, por ahora es un codigo fuera del contenedor. Su función es llamar a la api, para luego almacenar las respuestas en la base de datos MySQL.

## Flask:
Las rutas son para setear un cron desde afuera, cada ruta es una funcion, por ejemplo update-merval, ejecuta la funcion cada 50 segundos del chequeo de los valores
Le debería agregar otras rutas para refrescar otros valores.

## Documentacion

* PyMysql: https://pymysql.readthedocs.io/en/latest/user/examples.html
* PyMysql no oficial: http://zetcode.com/python/pymysql/#:~:text=PyMySQL%20fetchAll,as%20a%20sequence%20of%20sequences.&text=In%20the%20example%2C%20we%20retrieve%20all%20cities%20from%20the%20database%20table.&text=This%20SQL%20statement%20selects%20all%20data%20from%20the%20cities%20table.&text=The%20fetchall%20function%20gets%20all%20records.
* schedule: https://schedule.readthedocs.io/en/stable/
* Pyrebase: https://github.com/thisbejim/Pyrebase
* Firebase: https://console.firebase.google.com/
* Firebase Admin server: (credentials json) https://firebase.google.com/docs/admin/setup#python
* Firebase para humanos: https://medium.com/faun/getting-started-with-firebase-cloud-firestore-using-python-c6ab3f5ecae0
* Firestore example data python: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/cc1f10a38b4c0a37a87039fa4e9a7fd84b090e8b/firestore/cloud-client/snippets.py#L282-L282