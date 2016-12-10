

#!/bin/bash

#Fetch the code from bitbucket repo

cd /home/pi/pi-relay-app
sudo git checkout .
sudo git pull origin master


#Restart the service

sudo systemctl restart pi-relay.service