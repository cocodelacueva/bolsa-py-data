# Bolsa py data

Captura los datos de valores de la bolsa para volcarlos en algunas bases de datos.

## Datos api
* Invertir online (tiene un limite de llamadas por día)

## Bases de datos

* MySQL: Guarda los datos duros para analizarlos luego y volcarlos a la base de datos online.
* Firebase: Datos online, estos datos se consumen desde el front end.

## CODIGO

Armado en python, por ahora es un codigo fuera del contenedor. Su función es llamar a la api, para luego almacenar las respuestas en la base de datos MySQL.