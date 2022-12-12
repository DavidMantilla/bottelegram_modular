# Python module to diseno
import os
class  escaner: 
    
    def __init__(self) :
        self.dire = os.getenv('DIRE')
    def escan(self):
        try:
            os.system("scanimage  --mode=Color  --format=png>"+str(self.dire))
        except Exception as error:
            return error
        return open(str(self.dire), 'rb')
    