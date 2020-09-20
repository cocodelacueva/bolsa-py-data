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
* schedule: https://schedule.readthedocs.io/en/stable/
* Pyrebase: https://github.com/thisbejim/Pyrebase