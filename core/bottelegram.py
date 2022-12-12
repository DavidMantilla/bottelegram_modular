import time
import telebot
import os
from dotenv import load_dotenv
from config import bottelegram
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

            self.bot.reply_to(message, f"""Hola seleciona la opcion que necesites

        Impresora (🖨)  para self.imprimir

        Clima(🌡)  para conocer el clima

        escan (📷)  para escanear

        """)

        
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
            time.sleep(20)
        except KeyboardInterrupt:  # Clean exit
            telegram.stop_polling()
            print("Bot polling loop finished")
            break  # End loop
