
#!/bin/bash

#Fetch the code from bitbucket repo

cd /home/pi/pi-relay-app/
sudo git checkout .
sudo git pull origin master

sudo python3 stream-get.py


