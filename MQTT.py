#Imports needed to create the connection
from distutils.command.clean import clean
from http import client
from msilib.schema import AdminExecuteSequence
from xmlrpc.client import ProtocolError
import paho.mqtt.client
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from csv import writer

#connection to firebase
firebase_sdk = credentials.Certificate('YOUR_FIREBASE_CREDENTIALS')
firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'YOUR_URL_DATABSE'})


#Function that subscribes to the breaker with the username
def on_connect(client, userdata, flags, rc):
    print('connectado (%s)' % client._client_id)
    client.subscribe(topic='Prueba', qos=2)

#Function that fires as soon as the breaker receives a message
def on_message(client, userdata, message):
    print('------------------------')
    print('Topico: %s' % message.topic)
    payload = json.loads(message.payload)
    print('Mensaje: %s' % payload)
    detectado=str(payload['Detecta'])
    Tamano=str(payload['Tamano'])
    No = str(payload['No. Detectados'])
    print('qos: %d' % message.qos)
    print('------------------------')
    ref =db.reference('/brocolis')
    ref.push({
        "Detectado": detectado,
        "Tamano": Tamano,
        "No_Detectados": No
    })
    list_data=[detectado    ,Tamano,No]
    with open('datos.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(list_data)  
        f_object.close()


#Connection to PAHO MQTT breaker
def main():
    client = paho.mqtt.client.Client(client_id='YOUR_USERNAME', clean_session= False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host='YOUR_IP', port=1883)
    client.loop_forever()


if __name__ == '__main__':
    main()
