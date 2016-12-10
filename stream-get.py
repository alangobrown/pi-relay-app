
#Get the channel status from firebase

import platform as platform
if platform.platform()[0:5] == 'Linux':
  import RPi.GPIO as GPIO
else:
  import mockGPIO as GPIO 
import time


import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyAIQIGNFXAzjjWyFqy7FjxERAyU8XyJ9z4",
  "authDomain": "pi-relay.firebaseapp.com",
  "databaseURL": "https://pi-relay.firebaseio.com/",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "config/firebaseCredentials.json"
}
firebase = pyrebase.initialize_app(firebaseConfig)

#secret = f1ltsJ3sB8qhPdxD6fg57LijDEIAgThwYuY0qIWY


auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("alan@mailmob.co.uk", "!Z4PSK^#Lcc$qcjE")

db = firebase.database()

pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

def stream_handler(message):



    if(message["event"]=="put" and message["path"]=="/1"):
      #print(message["path"]) # /-K7yGTTEp7O549EzTYtI
      if (message["data"]["status"]==0):
        print("Detected the channel should be turned off")
        GPIO.output(pin,True)

      if (message["data"]["status"]==1):
        print("Detected the channel should be turned on")
        GPIO.output(pin,False)




my_stream = db.child("devices/alans-rpi-01").stream(stream_handler)