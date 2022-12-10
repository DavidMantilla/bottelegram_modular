import os
from datetime import datetime
import pymysql
from dotenv import load_dotenv

load_dotenv()


class conexion:
    host = os.getenv('HOST')
    user = os.getenv('DBUSER')
    pasword = os.getenv('PASSWORD')
    puerto = os.getenv('PUERTO')
    database = os.getenv('DATABASE')
    def __init__(self):
         self.dbConnect = pymysql.connect(host=self.host,
                                         user=self.user,
                                         password=self.pasword,
                                         database=self.database,
                                         cursorclass=pymysql.cursors.DictCursor)
         
    
    def consultaRetorno(self,sql):
        try:
            with self.dbConnect.cursor() as cursor:
                cursor.execute(sql)
                recordatorio = cursor.fetchall()
                cursor.close()
            return recordatorio
        except Exception as e:
           print(e)
    
    
    
    def consulta(self,sql):
       try: 
            with self.dbConnect.cursor() as cursor:
                cursor.execute(sql)
                self.dbConnect.commit()
                cursor.close()
            
       except Exception as e:
           print(e)
    
    def cerrar(self):
         self.dbConnect.close()
    
    
        

    