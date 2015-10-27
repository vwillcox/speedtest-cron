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

Setup email:

Now edit the file /etc/ssmtp/ssmtp.conf as root and add the next lines. Please note that some of the lines already exist and may need to be changed. Others don't exist yet and need to be added to the end of the file.

mailhub=smtp.gmail.com:587

hostname=ENTER YOUR RPI'S HOST NAME HERE

AuthUser=YOU@gmail.com

AuthPass=PASSWORD

useSTARTTLS=YES

Again you'll have to replace YOU with your email login name and PASSWORD with your (application specific) gmail password. 
After this you're done. You don't even have to restart the SSMTP server (in fact, there is none).

You can use other smtp servers if your ISP or hosting provide has them.

I am working on an installer - this will come in a later version once other bugs are fixed.
