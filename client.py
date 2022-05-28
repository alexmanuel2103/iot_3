from http import client
from wsgiref import headers
from gyroscope import Sensor
import json
import time

#Creación de un objeto de la clase HTTPConnection
_conn = client.HTTPConnection(host='localhost', port=5000)

#Creación de un objeto de la clase Sensor
s = Sensor()

#Para formar el JSON que se va para el servidor
h={'content-type':'application/json'}


while True:
    data={
    'id':1,
    'name': 'Temp sensor',
    'value': s.get_random_number()
    }
    json_data = json.dumps(data)
    #enviar datos al servidor
    _conn.request('POST', '/devices', json_data, headers=h)
    _conn.close(
    )
    
    print(s.get_random_number())
    #print(s.get_temp())
    time.sleep(15)

'''
    Lluvia de ideas:
    Quizá se pueda usar un if con la condición de "if (i<15)" se
    mantiene la inclinación de manera normal, pero en dado
    caso si se excede, hay que usar un elif para inclinar la
    plataforma a 0 grados.
'''