import time
import telebot
import os
from dotenv import load_dotenv
from config import bottelegram
import urllib
load_dotenv()


class botTelegram:
    chat = 0
    # Ponemos nuestro Token generado con el @BotFather
    TOKEN = os.getenv('TOKEN')
    nombreusuario = None

    def __init__(self):
        # Creamos nuestra instancia "self.bot" a partir de ese TOKEN
        self.bot = telebot.TeleBot(self.TOKEN)

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
        def echo_all(message):
            self.chat = message.chat.id
            self.nombreusuario = str(
                message.from_user.first_name)+' '+str(message.from_user.last_name)
            info=message.text.lower()
            config = ''
            retorno = ""
            menu=""
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
            else:
                for clase in bottelegram:
                    auxclase = bottelegram[clase]
                    for funcion in auxclase.keys():
                        if (funcion in info):
                          if (config == ''):
                            config = info
                            if (auxclase[funcion]['activo']):
                                param = auxclase[funcion]['params']
                                if (param != None and param != ''):
                                    params = param.copy()
                                    if ('validate' in auxclase[funcion] and 'comand' in auxclase[funcion]):
                                        dicc = auxclase[funcion]['validate'](info)
                                        menu = ""
                                        for param in params:
                                            if (type(dicc) == dict and param in dicc):
                                                params[param] = dicc[param]
                                            elif params[param] != "":
                                                if (type(params[param]) == list):
                                                    if (menu != ""):
                                                        if (params[param][1] == menu):
                                                            self.bot.send_message(self.chat,params[param][0])
                                                            params[param] = info
                                                            menu = ''

                                                    elif (params[param][1] == 'menu'):
                                                        self.bot.send_message(self.chat,params[param][0])
                                                        menu = info
                                                        params[param] = menu
                                                else:
                                                    self.bot.send_message(self.chat,params[param])
                                                    params[param] = info

                                        retorno = auxclase[funcion]['funcion'](params)
                                        break

                                    else:
                                        self.bot.send_message(self.chat,'se ha declarado mal esta funcion')

                                else:
                                    retorno = auxclase[funcion]['funcion']()                                  
                                    break

                if (config == ''):
                  self.bot.send_message(self.chat,"no se ha configurado esta opcion")
                  config = ''

                if (type(retorno) == str):
                  self.bot.send_message(self.chat,retorno)
        @self.bot.message_handler(content_types=['document', 'photo'])
        def getdoc(message):  
          if (message.content_type == "document"):
            for clase in bottelegram:
                    auxclase = bottelegram[clase]
                    for funcion in auxclase.keys():
                      if 'content_types' in auxclase[funcion]:
                        file = self.bot.get_file(message.photo[0].file_id)
                        archivo = "https://api.telegram.org/file/bot"+self.TOKEN+"/"+file.file_path
                        print(archivo)
                        urllib.request.urlretrieve(archivo, "./"+file.file_path)
                        retorno=auxclase[funcion]['funcion'](file.file_path)
                        self.bot.send_message(retorno)
                         
                  
                        
            
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
