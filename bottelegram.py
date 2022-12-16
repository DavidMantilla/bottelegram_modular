import time
import telebot
import os
from dotenv import load_dotenv
from config import bottelegram
from models import conexion
import urllib
load_dotenv()


class botTelegram:
    chat = 0
    # Ponemos nuestro Token generado con el @BotFather
    TOKEN = os.getenv('TOKEN')
    nombreusuario = None
    auxparam = ""
    auxfuncion=""
    config = ''
    menu = ''
    paramCount=0

    def __init__(self):
        # Creamos nuestra instancia "self.bot" a partir de ese TOKEN
        self.bot = telebot.TeleBot(self.TOKEN)
        self.conexion = conexion()
    
    def initchat(self):
      result=self.conexion.consultaRetorno('select * from chat  where chatid ="{}"'.format(self.chat))
      if():
        pass

    def accionesMsg(self, message):
      try:
            
            retorno = ""
            self.nombreusuario = str(
                message.from_user.first_name)+' '+str(message.from_user.last_name)

            info = ""
            if (self.auxparam != "" and type(self.auxparam)==dict):
              auxp=[*self.auxparam][self.paramCount]
              print("posicion",auxp)
              if self.paramCount+1>=len(self.auxparam.keys()) : 
                if self.auxparam[auxp]!="":
                  if (type(self.auxparam[auxp]) == str):
                    self.auxparam[auxp]=message.text.lower()
                    retorno=self.auxfuncion["funcion"](self.auxparam)
                    self.auxparam=""
                    self.paramCount=0
                    self.auxfuncion=""
                    self.config=''
                    self.bot.send_message(self.chat, retorno)
                  else:
                    menu=self.auxparam[auxp][1].copy()
                    print(menu)
                    self.auxparam[auxp]=message.text.lower()  
                    print("param",self.auxparam[auxp])              
                    if(self.auxparam[auxp].lower()=="si"):
                      self.auxparam["dias"]=menu["dias"]
                    else:
                      self.auxparam["fecha"]=menu["fecha"]
                    self.paramCount+=1
                    auxp=[*self.auxparam][self.paramCount]
                    self.bot.send_message(self.chat, self.auxparam[auxp])
                    
                 
              else:
                if self.auxparam[auxp]!="":
                  if (type(self.auxparam[auxp]) == str):
                    self.auxparam[auxp]=message.text.lower()                
                    self.paramCount+=1
                    auxp=[*self.auxparam][self.paramCount]
                    self.bot.send_message(self.chat, self.auxparam[auxp])
                  else:
                    menu=self.auxparam[auxp][1].copy()
                    self.auxparam[auxp]=message.text.lower()                
                    if(self.auxparam[auxp]=="si"):
                      self.auxparam["dia"]=menu["dia"]
                    else:
                      self.auxparam["fecha"]=menu["fecha"]                     
                    print("dia-",self.auxparam)
                    self.paramCount+=1
                    auxp=[*self.auxparam][self.paramCount]
                    self.bot.send_message(self.chat, self.auxparam[auxp])
            else:
              info = message.text.lower()
            print("info",info,"auxparam",self.auxparam)
            if (info == "hola"):
                clasgroup = ""
                self.bot.reply_to(
                    message, f"""Hola {self.nombreusuario} seleciona la opcion que necesites""")
                for clase in bottelegram:
                    anterior = ""
                    mensaje = ""
                    clasgroup += clase+"\n"
                    for funcion in bottelegram[clase]:
                        auxclase = bottelegram[clase]
                        if auxclase[funcion]['grupo'] != None:
                            if (not 'secundary' in auxclase[funcion] and anterior != "" and anterior['grupo'] == auxclase[funcion]['grupo']):
                                if (auxclase[funcion]['activo']):
                                    clasgroup += ' -' + mensaje + \
                                        '(' + funcion + ')'+'\n'

                        else:
                            if (not 'secundary' in auxclase[funcion] and anterior != ""):
                                if (auxclase[funcion]['activo']):
                                    clasgroup += ' (' + funcion + ')\n'

                        anterior = auxclase[funcion]
                        mensaje = funcion
                self.bot.send_message(self.chat, clasgroup)
            elif (info != ""):
              for clase in bottelegram:
                    auxclase = bottelegram[clase]
                    for funcion in auxclase.keys():
                        palabras = info.split(' ')[:2]
                        opcion = " ".join(palabras)
                        if (funcion in opcion):
                          if (self.config == ''):
                            self.config = info
                            if (auxclase[funcion]['activo']):
                                param = auxclase[funcion]['params']
                                if (param != None and param != ''):
                                    params = param.copy()
                                    if ('validate' in auxclase[funcion] and 'comand' in auxclase[funcion]):
                                        dicc = auxclase[funcion]['validate'](
                                            info)
                                        self.menu = ""
                                        for param in params:
                                            if (type(dicc) == dict and param in dicc):
                                                params[param] = dicc[param]
                                                self.paramCount+=1
                                            elif params[param] != "":
                                                if (type(params[param]) == list):
                                                    if (self.menu == ""):
                                                        self.bot.send_message(
                                                            self.chat, params[param][0])
                                                        self.auxmenu = True
                                                        self.auxparam = params
                                                        return

                                                else:
                                                    self.bot.send_message(
                                                        self.chat, params[param])
                                                    self.auxparam = params
                                                    self.auxfuncion=auxclase[funcion]
                                                    return
                                            
                                        retorno = auxclase[funcion]['funcion'](
                                            params)
                                        break

                                    else:
                                        self.bot.send_message(
                                            self.chat, 'se ha declarado mal esta funcion')
                                        self.config=""

                                else:
                                    retorno = auxclase[funcion]['funcion']()
                                    break

              if (self.config == ''):
                self.bot.send_message(
                    self.chat, "no se ha configurado esta opcion")
                self.config = ''

              if (type(retorno) == str):
                self.bot.send_message(self.chat, retorno)
                self.auxparam = ""
                self.config = ""
      except Exception as error:
        print(error)      
      

    def acciones(self):
        @self.bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            self.chat = message.chat.id
            clasgroup = ""
            self.nombreusuario = str(
                message.from_user.first_name)+' '+str(message.from_user.last_name)

            self.bot.reply_to(
                message, f"""Hola {self.nombreusuario} seleciona la opcion que necesites""")
            for clase in bottelegram:
                anterior = ""
                mensaje = ""
                clasgroup += clase+"\n"
                for funcion in bottelegram[clase]:
                    auxclase = bottelegram[clase]
                    if auxclase[funcion]['grupo'] != None:
                        if (not 'secundary' in auxclase[funcion] and anterior != "" and anterior['grupo'] == auxclase[funcion]['grupo']):
                            if (auxclase[funcion]['activo']):
                                clasgroup += ' -' + mensaje + \
                                    '(' + funcion + ')'+'\n'

                    else:
                        if (not 'secundary' in auxclase[funcion] and anterior != ""):
                            if (auxclase[funcion]['activo']):
                                clasgroup += ' (' + funcion + ')\n'

                    anterior = auxclase[funcion]
                    mensaje = funcion
            self.bot.send_message(self.chat, clasgroup)

        @self.bot.message_handler(func=lambda message: True)
        def message(message):
          self.chat = message.chat.id
          self.accionesMsg(message)
            
        @self.bot.message_handler(content_types=['document'])
        def getdoc(message):  
          if (message.content_type == "document"):
            
            for clase in bottelegram:
                    auxclase = bottelegram[clase]
                    for funcion in auxclase.keys():
                        if 'content_types' in auxclase[funcion]:
                          file = self.bot.get_file(message.document.file_id)
                          archivo = "https://api.telegram.org/file/bot"+self.TOKEN+"/"+file.file_path
                          print(archivo)
                          urllib.request.urlretrieve(archivo, "./"+file.file_path)
                          retorno=auxclase[funcion]['funcion'](file.file_path)
                          self.bot.send_message(self.chat,retorno)
                          
                  
                        
            
    def polling(self):
        self.bot.polling(none_stop=True, interval=3, timeout=30)

    def stop_polling(self):
        self.bot.stop_polling()


if __name__ == "__main__":

    while True:

        try:
            telegram = botTelegram()
            telegram.acciones()
            telegram.polling()
        except Exception as ex:  # Error in polling
            print("Bot polling failed, restarting in {}sec. Error:\n{}".format(30, ex))
            telegram.stop_polling()
            time.sleep(2)
        except KeyboardInterrupt:  # Clean exit
            telegram.stop_polling()
            print("Bot polling loop finished")
            break  # End loop
