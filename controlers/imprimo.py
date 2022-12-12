# Python module to diseno
import cups
from models import conexion


class imprimo:
    imprimir = False
    doc = False

    def __init__(self):
        self.imprimir = False
        self.conexion = conexion()

    def print(self):
        if (self.imprimir):
            self.imprimir = False
            self.doc = True
            return "envia documento"

    def setImprimir(self):
        self.imprimir = True
        return 'desea imprimir'

    def document(self, url='documents/file_6.png'):
        if (self.doc):
            try:
                conn = cups.Connection()
                printers = conn.getPrinters()
                for printer in printers:
                    print(printer, printers[printer]["device-uri"])

                # printer_name=list(conn.getPrinters().keys())[1]
                printer_name = conn.getDefault()
                # fileName = "documents/file_6.png"
                printinfo = conn.printFile(
                    printer_name, url, " ", {})
                impresion = [printinfo, conn.getJobAttributes(printinfo)[
                    "job-state"]]
                self.conexion.consulta(
                    f'INSERT INTO `impresion`( `idimpresion`, `estado`, `enviado`, `chat`, `fecha`) VALUES ("{impresion[0]}","{impresion[1]}","{0}","{id}",curdate())')
                return "Imprimiendo"
            except Exception as e:
                print("ha ocurrido un error "+repr(e))

    def infoPrint():
        pass
