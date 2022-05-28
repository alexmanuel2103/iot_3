from random import randint
import psutil

#POO en Python
#Definición de la clase
class Sensor:
    
    #Constructor de la clase
    def __init__(self):
        self.sensor = psutil.sensors_temperatures()

    def get_temp(self):
        return self.sensor['coretemp']

    #Simula la toma de algun valor de otro sensor
    def get_random_number(self):
        return randint(0,90)