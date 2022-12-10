# Python module to recordatorio
from models import conexion
from controlers import clima
import json
from datetime import datetime
import re

class recordatorio:
    dict_recorda = {"repetir": "",
                    "tipo": "",
                    "fecha": '',
                    "hora": "",
                    "descripcion": '',
                    "dias": "",
                    "chat": "",
                    "estado": "",
                    }
    diasArray = ["lun", "mar", "mie", "jue", "vie", "sab", "dom"]
    error=False
    def __init__(self):
        self.conexion = conexion()
        self.clima=clima.clima()
        
    def pasos(self,value):
        print("pasos",value)
        self.error=False
        fecha=""
        am=""
        minu=""
        for clave, value in value.items():
            if(type(value)!= list):
                self.dict_recorda[clave]=value
                if clave=="hora" and len(value.lower().split(":")) >1 : 
                    hour = value.split(":")[0]
                    minute = value.split(":")[1]
                    
                    if (len(minute.split(" ")) > 1):
                        am = str(minute[2:5]).lstrip()
                        minu = minute[0:2]
                    else:
                        am = minute[2:5]
                        minu = minute[0:2]
                    
                    # Convertir la hora a un entero
                    hour_24 = int(hour)
                    print(hour_24)
                    # Si la hora es pm y es diferente de 12, sumar 12 para convertirla a formato de 24 horas
                    if am == "pm" and hour_24 != 12:
                        hour_24 += 12
                        print(hour_24)
                        

                    # Si la hora es am y es igual a 12, restar 12 para convertirla a formato de 24 horas
                    if am == "am" and hour_24 == 12:
                        hour_24 -= 12
                        print(hour_24)

                    # Convertir la hora de nuevo a una cadena de texto y agregar los minutos
                    hour_24_str = str(hour_24)
                    fecha = hour_24_str + ":" + str(minu)

                    print(fecha)
                    self.dict_recorda[clave]=fecha
                elif(clave=="hora"):
                    self.error=True
                    print(clave,value)
                if clave=="fecha" and len(value.lower().split("/")) >1 :
                    self.dict_recorda[clave]=value
                elif(clave=="fecha"):
                    print(clave,value)
                    self.error=True
                if clave=="repetir":
                    self.dict_recorda[clave]=1 if value=="si" else 0
                if clave=="dias":
                    rango = len(value.lower().split("-"))
                    dias = len(value.lower().split(","))
                    dia = value.lower() in self.diasArray
                    if (rango > 1 or dias > 1 or dia):
                        dictDias = {}
                        if (dia):
                            dictDias[value.lower()] = 1
                        else:
                            if (rango > 1):

                                min = self.diasArray.index(
                                    value.lower().split("-")[0])
                                max = self.diasArray.index(
                                    value.lower().split("-")[1])
                                for x in self.diasArray:
                                    if (min <= self.diasArray.index(x) and max >= self.diasArray.index(x)):
                                        dictDias[x] = 1
            
                            else:
                                for x in value.lower().split(","):
                                    dictDias[x] = 1

                        self.dict_recorda[clave] = dictDias
            else:
                if clave=="fecha":
                    self.dict_recorda[clave] = None
                
        if(self.error):
           return "ha habido un error"
        else:                           
            self.dict_recorda['estado'] = 1
            self.guardar()
            return "guardado"
                

    def guardar(self):
        if(self.dict_recorda["fecha"]==None):
            self.conexion.consulta(
                f'INSERT INTO `recordatorio`(`repetir`,`tipo`, `hora`, `descripcion`, `dias`, `chat`, `estado`) VALUES ("{self.dict_recorda["repetir"]}","{self.dict_recorda["tipo"]}","{self.dict_recorda["hora"]}","{self.dict_recorda["descripcion"]}",\'{json.dumps(self.dict_recorda["dias"])}\',"{self.dict_recorda["chat"]}","{self.dict_recorda["estado"]}")')
        else:
            self.conexion.consulta(
            f'INSERT INTO `recordatorio`(`repetir`,`tipo`,fecha ,`hora`, `descripcion`, `dias`, `chat`, `estado`) VALUES ("{self.dict_recorda["repetir"]}","{self.dict_recorda["tipo"]}","{self.dict_recorda["fecha"]}","{self.dict_recorda["hora"]}","{self.dict_recorda["descripcion"]}",\'{json.dumps(self.dict_recorda["dias"])}\',"{self.dict_recorda["chat"]}","{self.dict_recorda["estado"]}")')

    def actualizar(self,texto):
        array = self.buscar(actualiza=True)
        if(array['tipo']==0):
            self.conexion.consulta(f'update recordatorio set estado=0 where id= "{str(array["id"])}"')
        else:
            if(texto=="ok"):
                diasemana = datetime.today().weekday()
                dia=json.loads(array["dias"])
                dia[self.diasArray[diasemana]]=0
                self.conexion.consulta(f'update recordatorio set dias=\'{json.dumps(dia)}\' where id= "{str(array["id"])}"')
            elif(texto=="desactivar"):
                self.conexion.consulta(f'update recordatorio set estado=0 where id= "{str(array["id"])}"')

            
    def buscar(self,actualiza=None):
        recordatorio=self.conexion.consultaRetorno(
            'select * from recordatorio as rec left join chat on chat.id =rec.chat where estado=1')
        if len(recordatorio)>0:
            for array in recordatorio:
                hora = datetime.strptime(array["hora"], "%H:%M")
                ahoratime = datetime.strptime(
                    datetime.now().strftime("%H:%M"), "%H:%M")
                diff = ahoratime-hora
                min = int(diff.total_seconds()/60)

                if (min >= -10 and min < 10):
                    if (min == -10 or min == -5 or min == 0 or min == 5 or min == 9):
                        array["enviado"] = 1
                        if (array["tipo"] == "despertador"):
                            array['descripcion'] = self.clima.mostrar()
                        if(actualiza):
                            return array
                        else:
                            return array["chatid"], array['descripcion']
                        
        else:
            return 'no hay un recordatorio'
    
    def mostrar(self):
        retorno=""
        recordatorio = self.conexion.consultaRetorno(
            'select * from recordatorio as rec left join chat on chat.id =rec.chat where estado=1')
        for dic in recordatorio :
           retorno+= dic['tipo']+" "+dic['hora']+" "+dic['descripcion']+"\n"
        return retorno
    def validate(self,text):
        dic={'tipo':0}
        descripcion=""
        
        if  len(text.split(' '))>1:
            texto=text.split(' ')
            dic['tipo']= texto[0]
            
            if ':' in text:
                hora=[str(s) for s in re.findall(r'-?\d+\.?\d*', text)]
                am= "pm" if text.find("pm", 0,len(text))!=-1 else "am"
                dic['hora']= str(hora[0])+":"+str(hora[1])+' '+am
                
            if(dic["tipo"]=="recuerdame" or dic["tipo"]=="recuérdame" ):
                    dsc=texto[1:len(text)]
                    for desc in dsc:
                        descripcion+=desc+" "
                    dic["descripcion"]=descripcion
            if('minutos' in text or 'minuto' in text or 'min' in text):
                fecha=datetime.now()
                dic["fecha"]=fecha.strftime("%Y/%m/%d")
                min= fecha.strftime("%M")
                minute=[str(s) for s in re.findall(r'-?\d+\.?\d*', text)]
                minute=int(minute[0])
                dic["hora"]=fecha.strftime("%H")+":"+ str(int(min)+minute)
                dic["repetir"]=0
        else:
           dic['tipo']= text
           
            
        return dic
    
 