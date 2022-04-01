#Imports needed to create the connection
from distutils.command.clean import clean
from http import client
from xmlrpc.client import ProtocolError
import paho.mqtt.client as mqtt

#Example function of sending a message to the breaker
def main():
    client = mqtt.Client()
    client.connect(host='127.0.0.1', port=1883)
    client.publish('Prueba', '{temperatura:20,lugar:DH}')


if __name__ == '__main__':
    main()