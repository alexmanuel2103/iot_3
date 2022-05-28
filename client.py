from http import client
from wsgiref import headers
from iot_device import Sensor #IMPORT IOT_DEVICE CLASS
import json
import time

#OBJECT CREATION FOR HTTPCONNECTION CLASS
_conn = client.HTTPConnection(host='localhost', port=5000)

#OBJECT CREATION FOR SENSOR CLASS
s = Sensor()

#H IS USED TO CREATE A .JSON FILE WHICH WILL BE SENT TO SERVER.
h={'content-type':'application/json'}


while True:
    data={
    'id':1,
    'name': 'Proximity Sensor', #SENSOR NAME
    'value': s.get_random_number() #RANDOM NUMBER GENERATOR
    }
    json_data = json.dumps(data)
		#SENDS DATA TO SERVER
    _conn.request('POST', '/devices', json_data, headers=h)#ENDPOINT WITH POST METHOD AND ENPOINT DEVICES
    _conn.close(
    )
    print(s.get_random_number())#PRINT THE RANDOM NUMBER
    #print(s.get_temp())
    time.sleep(1)#TIME LATENCY