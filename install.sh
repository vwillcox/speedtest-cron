#!/usr/bin/env bash
# Network Testing Appliance
# Uses the speedtest.net servers and SpeedTest-CLI
# SpeedTest-cli by Matt Martz

# Version 1 - Simple Speed Testing
# Installer Script (run as root/sudo please)

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi
  function pause(){
   read -p "$*"
}
 
echo "Welcome to The Network Testing Appliance Installer"
pause 'Press [Enter] to install the required bits and peices or CTRL+C to stop...'
echo "Installing mpack zip ssmtp mailutils mpack python-pip python3-pip python-w1thermsensor python3-w1thermsensor python-spidev python3-spidev"
apt-get install mpack zip ssmtp mailutils mpack python-pip python3-pip python-w1thermsensor python3-w1thermsensor python-spidev python3-spidev -y 2>&1 >/dev/null
echo "Done"
echo "Now installing python modules: gpiozero, speedtest-cli and ipgetter"
pip install gpiozero 2>&1 >/dev/null
pip3 install gpiozero 2>&1 >/dev/null
pip install speedtest-cli 2>&1 >/dev/null
pip install ipgetter 2>&1 >/dev/null
pip3 install ipgetter 2>&1 >/dev/null
echo "All done! Enjoy"

