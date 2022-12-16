# configuracion de modulos del bot

## Estructura del proyecto

1. controlers
   * \_\_init__.py  _aqui se debe declarar_
   * clima.py
   * escaner.py
   * imprimo.py
   * recordatorio.py
   * spotify.py
   * _aqui se puede agregar un modulo nuevo_
  
2. documents _archivos estaticos_
3. models
   * \_\_init__.py
   * conexion.py _archivo de conexion_
4. .env
5. config.py _archivo de configuracion_
6. index.py _core de la aplicacion_  

### config.py

import controlers **declaracion**

**inicializacion de las clases**  
spotify = controlers.spotify()  
clima = controlers.clima()  
escaner = controlers.escaner()  
imprimir = controlers.imprimo()  
recordatorio = controlers.recordatorio()

**Diccionario de  creacion del menu**
bottelegram = {'clase': {  
    'comando a usar':  
{
  'funcion': recordatorio.pasos,  
             "activo": True,  
             'grupo': 'despiertame',  
             'params': {  
             "tipo": "",  
             "hora": "envia la hora",  
             "repetir": ["desea repetir",  'menu'],  
             "fecha": ['escriba la fecha aa/mm/dd','no'],  
             "dias": ["escribe los dias lun,mar,mie,jue,vie,sab,dom ,  (lun-vie) ",'si'],  
             "chat": "",  
},  
           'validate':recordatorio.       validate,
           'comand': True},

**clase**  
es el objeto inicializado en laparte de arriba del documento

**comando a usar**
palabra clave o parte de la palabra clave a usar

**funcion**  
es la acción a ejecutar por medio del comando

**activo**  
es el estado de la función

**params**
son los parametros que debe recibir la función
debe ser un diccionario  

{nombre:valor }

validate (texto)

### Documentación del objeto bottelegram

Este objeto contiene información sobre diferentes comandos y funciones que se pueden usar en una aplicación de Telegram.

Estructura del objeto
bottelegram = {
  'spotify': {
    ...
  },  
  'clima': {
    ...
  },  
  'escaner': {
    ...
  },  
  'imprimo': {
    ...
  },  
  'recordatorio': {
    ...
  }   
}  
El objeto bottelegram tiene cinco propiedades principales: spotify, clima, escaner, imprimo y recordatorio. Cada una de estas propiedades es un objeto que contiene información sobre diferentes comandos y funciones relacionados con un tema en particular.  

Propiedades y valores del objeto
spotify: este objeto contiene información sobre comandos y funciones relacionados con Spotify.  
clima: este objeto contiene información sobre comandos y funciones relacionados con el clima.  
escaner: este objeto contiene información sobre comandos y funciones relacionados con el escaneo de documentos.  
imprimo: este objeto contiene información sobre comandos y funciones relacionados con la impresión de documentos.  
recordatorio: este objeto contiene información sobre comandos y funciones relacionados con el recordatorio de eventos y tareas.  
Cada uno de estos objetos tiene propiedades adicionales que representan diferentes comandos y funciones. Por ejemplo, el objeto spotify tiene las propiedades spotify info, busca, reproduce lista, reproducir lista, mis cantantes, ultima cancion y mis listas. Cada una de estas propiedades es un objeto que contiene información sobre un comando específico, como la función que se debe llamar cuando se ejecute el comando y los parámetros que se le deben proporcionar.  

### Ejemplos de uso

Aquí hay unos ejemplos de cómo se pueden usar los comandos y funciones definidos en el objeto bottelegram:


// Mostrar información sobre la cuenta de Spotify del usuario  

bottelegram.spotify['spotify info']

Este código es un bot de Telegram desarrollado en Python. El bot se inicializa utilizando el token generado por BotFather, y se utiliza la librería telebot para crear la instancia del bot y gestionar sus mensajes. El código utiliza la función message_handler de la librería telebot para definir las acciones que el bot realizará cuando reciba distintos tipos de mensajes. Cuando el bot recibe un mensaje que contenga los comandos start o help, enviará un mensaje de bienvenida y una lista de opciones disponibles. Si recibe cualquier otro tipo de mensaj

