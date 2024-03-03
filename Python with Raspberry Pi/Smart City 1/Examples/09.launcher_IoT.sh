
#!/bin/sh
#launcher.sh

cd /
cd home/pi/raspi-IoT
for i in {1..60}; do ping -c1 www.google.com &> /dev/null && break; done
sudo python flask_app.py
cd /
