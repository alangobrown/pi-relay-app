
#Get the channel status from firebase


import pyrebase
config = {
  "apiKey": "AIzaSyAIQIGNFXAzjjWyFqy7FjxERAyU8XyJ9z4",
  "authDomain": "pi-relay.firebaseapp.com",
  "databaseURL": "https://pi-relay.firebaseio.com/",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "config/firebaseCredentials.json"
}
firebase = pyrebase.initialize_app(config)

#secret = f1ltsJ3sB8qhPdxD6fg57LijDEIAgThwYuY0qIWY


auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("alan@mailmob.co.uk", "!Z4PSK^#Lcc$qcjE")


db = firebase.database()

channels = db.child("devices").child("alans-rpi-01").get()
print(channels.val())