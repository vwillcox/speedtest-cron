# speedtest-cron
A Simple set of scripts using Speedtest-cli to run hourly/half-hourly speed tests and email you the results.

To use this code you will need to install some dependancies

You will need gpioZero

http://pythonhosted.org/gpiozero/

sudo apt-get install python-pip python3-pip python-w1thermsensor python3-w1thermsensor python-spidev python3-spidev

sudo pip install gpiozero
sudo pip-3.2 install gpiozero

sudo pip install speedtest-cli

sudo pip install ipgetter

sudo pip3 install ipgetter

For the email sections you will need:

sudo apt-get install mpack zip ssmtp mailutils mpack

I am working on an installer - this will come in a later version once other bugs are fixed.
