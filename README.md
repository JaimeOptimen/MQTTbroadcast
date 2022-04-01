# MQTTbroadcast
To be able to make the connection through MQTT, you first need the imports of the paho mqtt and firebase libraries, which are not installed by default with python, so it is necessary to install them using:

-pip install firebase-admin command to install the firebase library. 

-and to install what is needed for the mqtt breaker is pip install paho-mqtt.

For the necessary part to create the breaker with mqtt it would be everything,
but for the part of the database connection it is necessary to first create an account previously within the official firebase page https://firebase.google.com

If you don't know how to create a database here is a tutorial on how you could do it https://www.youtube.com/watch?v=vcR9a6E2BOE. Once you have your project and database created, you need to have the following two things to be able to make the connection: a private access key that you can use to connect to the database, otherwise you will not have access, and second, the URL of the database.
To get the private keys you need to do this:

**1. First you need to go to the configuration part and in the users and permissions section click**
<p align="center"> 
  <img src="https://user-images.githubusercontent.com/102833881/161350808-eccbd31d-21ba-4450-a4af-c022290da39f.png" /> 
</p>

**2. Second go to the service accounts section, and in the SDK Firebase Admin section generate the key according to the language you need**
<p align="center"> 
  <img src="https://user-images.githubusercontent.com/102833881/161350495-5ac4ba06-8fce-474d-85bd-63b43cdfeb46.png" /> 
</p>
To get the URL of the database you need the following:
Within the menu we go to the Realtime Database section at the top of our table a URL will appear, we will only click on it and that will be our URL


<p align="center"> 
  <img src="https://user-images.githubusercontent.com/102833881/161351821-83520fd6-08fb-44e5-9eed-c47a66439894.png" /> 
</p>
