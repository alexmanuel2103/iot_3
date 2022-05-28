from random import randint
import psutil

#Definición de la clase
#CLASS DEFINITION
class Sensor:
    
    #Constructor de la clase
    #CLASS CONSTRUCTOR
    def __init__(self):
        self.sensor = psutil.sensors_temperatures()

    def get_temp(self):
        return self.sensor['coretemp']

    #CAPTURES THE VALUE OF THE SENSOR
    def get_random_number(self):
        return randint(0,100)