# Python module to __main__
from config import bottelegram
from models import conexion



if __name__ == "__main__":
    con = conexion()
  
    while True:
      config = ''
      retorno = ""
      info = input()
      menu=""
      if (info == "hola"):
          print(f"""Hola seleciona la opcion que necesites       """)
          for clase in bottelegram:
            anterior = ""
            mensaje = ""
            print(clase)
            for funcion in bottelegram[clase]:
              auxclase = bottelegram[clase]
              if auxclase[funcion]['grupo'] != None:

                if (not 'secundary' in auxclase[funcion] and anterior != "" and anterior['grupo'] ==auxclase[funcion]['grupo']):
                  if (auxclase[funcion]['activo']):
                    print('-', mensaje, '(', funcion, ')')

              else:
                  if (not 'secundary' in auxclase[funcion] and anterior != ""):
                    if (auxclase[funcion]['activo']):
                        print('-', funcion)

              anterior = auxclase[funcion]['funcion'].__name__
              mensaje = funcion

      else:
        for clase in bottelegram:
          auxclase = bottelegram[clase]
          for funcion in auxclase.keys():
            if (funcion in info):
              if(config==''):
                config=info
              if (auxclase[funcion]['activo']):
                param=auxclase[funcion]['params']
                if (param != None and param != ''):
                  params=param.copy()
                  if ('validate' in auxclase[funcion] and 'comand' in auxclase[funcion]):
                    dicc = auxclase[funcion]['validate'](info)
                    menu = ""
                    for param in params:
                      if (type(dicc)== dict and param in dicc):
                          params[param] = dicc[param]
                      elif params[param] != "":
                        if (type(params[param]) == list):
                            if (menu != ""):
                              if (params[param][1] == menu):
                                print(params[param][0])
                                params[param] = input()
                                menu = ''
                              

                            elif (params[param][1] == 'menu'):
                                print(params[param][0])
                                menu = input()
                                params[param] = menu
                        else:
                          print(params[param])
                          params[param] = input()
                    
                    retorno=auxclase[funcion]['funcion'](params)
                    break
  
                  else:
                   print('se ha declarado mal esta funcion')
                   
                else:
                  retorno=auxclase[funcion]['funcion']()
                  break
              
             
                   
        if(config==''):      
          print("no se ha configurado esta opcion")
          config=''
        
        
        if(type(retorno)== str):
           print(retorno)
        
            
          
      