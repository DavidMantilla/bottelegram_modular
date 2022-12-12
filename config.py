import controlers

spotify = controlers.spotify()
clima = controlers.clima()
escaner = controlers.escaner()
imprimir = controlers.imprimo()
recordatorio = controlers.recordatorio()

lista = spotify.listas()

bottelegram = {'spotify': {
    'spotify info':
    {'funcion': spotify.info,
     "activo": True,
     'params': None,
     'grupo': None},
    'busca': {'funcion': spotify.buscar,
              "activo": True,
              'params': {"search": "que cancion deseas"},
              'validate': spotify.validateBuscar,
              'comand': True,
              'grupo': None},
    'reproduce lista':
                        {'funcion': spotify.lista,
                        "activo": True,
                        'params': {
                        "lista": "cual lista te reproduzco "+lista,

                        },
                        'validate': spotify.validateLista,
                        'comand': True,
                        'grupo': 'lista'},
    'reproducir lista':
                        {'funcion': spotify.lista,
                        "activo": True,
                        'params': {
                        "lista": "cual lista te reproduzco "+lista,

                        },
                        'validate': spotify.validateLista,
                        'comand': True,
                        'grupo': 'lista'},
    'mis cantantes':
                    {'funcion': spotify.followed,
                     "activo": True,
                     'params': None,
                     'grupo': None},
    'ultima cancion':
                    {'funcion': spotify.recently,
                     "activo": True,
                     'params': None,
                     'grupo': None},
    'mis listas':
                {'funcion': spotify.listas,
                    "activo": True,
                    'params': None,
                    'grupo': None},
},
    'clima': {
        'clima': {'funcion': clima.mostrar,
                  "activo": True,
                  'params': None,
                  'grupo': 'clima'},
        '🌡': {'funcion': clima.mostrar,
              "activo": True,
              'params': None,
              'grupo': 'clima'},
},
    'escaner': {
        'escan': {'funcion': escaner.escan,
                  "activo": True,
                  'params': None,
                  'grupo': 'escan'},
        '📷': {'funcion': escaner.escan,
              "activo": True,
              'params': None,
              'grupo': 'escan'},
},
    'imprimo': {
        'imprimir':
            {'funcion': imprimir.setImprimir,
            "activo": True,
            'params': None,
            'grupo': 'print'},
        '🖨':
             {'funcion': imprimir.setImprimir,
             "activo": True,
             'params': None,
             'grupo': 'print'},
        'si':
            {'funcion': imprimir.print,
             "activo": True,
            'params': None,
            'grupo': None,
            'params': None,
            'secundary': True},
        'doc': {
            'funcion': imprimir.document,
            "activo": False,
            'params': None,
            'secundary': True,
            'grupo': None,
            'content_types':"document"},
},
    'recordatorio': {
        'despiertame': {
                        'funcion': recordatorio.pasos,
                        "activo": True,
                        'grupo': 'despiertame',
                        'params': {
                        "tipo": "",
                        "hora": "envia la hora",
                        "repetir": ["desea repetir", 'menu'],
                        "fecha": ['escriba la fecha aa/mm/dd', 'no'],
                        "dias": ["escribe los dias lun,mar,mie,jue,vie,sab,dom ,  (lun-vie) ", 'si'],
                        "chat": "",
                        },
                        'validate': recordatorio.validate,
                        'comand': True},
        'despiértame': {
                        'funcion': recordatorio.pasos,
                        "activo": True,
                        'grupo': 'despiertame',
                        'params': {
                        "tipo": "",
                        "hora": "envia la hora",
                        "repetir": ["desea repetir", 'menu'],
                        "fecha": ['escriba la fecha aa/mm/dd', 'no'],
                        "dias": ["escribe los dias lun,mar,mie,jue,vie,sab,dom ,  (lun-vie) ", 'si'],
                        "chat": "",

                        },
                        'validate': recordatorio.validate,
                        'comand': True},
        'recuerdame': {
                        'funcion': recordatorio.pasos,
                        "activo": True,
                        'grupo': 'recuerdame',
                        'params': {
                        "tipo": "",
                        "descripcion": 'que te debo recordar',
                        "hora": "envia la hora",
                        "repetir": ["desea repetir", 'menu'],
                        "fecha": ['escriba la fecha aa/mm/dd', 'no'],
                        "dias": ["escribe los dias lun,mar,mie,jue,vie,sab,dom ,  (lun-vie) ", 'si'],
                        "chat": "",
                        },
                        'validate': recordatorio.validate,
                        'comand': True},
        'recuérdame': {
                        'funcion': recordatorio.pasos,
                        "activo": True,
                        'grupo': 'recuerdame',
                        'params': {
                        "tipo": "",
                        "descripcion": '',
                        "hora": "envia la hora",
                        "repetir": ["desea repetir", 'menu'],
                        "fecha": ['escriba la fecha aa/mm/dd', 'no'],
                        "dias": ["escribe los dias lun,mar,mie,jue,vie,sab,dom ,  (lun-vie) ", 'si'],
                        "chat": "",
                        },
                        'validate': recordatorio.validate,
                        'comand': True},
        'mostrar recordatorios': {
                  'funcion': recordatorio.mostrar,
                  'activo': True,
                  'params': None,
                  'grupo': None,
                  'secundary': True},
        'ok': {
                'funcion': recordatorio.actualizar,
                'activo': True,
                'params': None,
                'grupo': None,
                'secundary': True},


}


}
