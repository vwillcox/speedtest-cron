# speedtest-cron
This application will run speedtest-cli against speedtest.net's servers using cron. It will then email the results daily and weekly.

Also - using http://www.percheron-electronics.uk/shop/ e-paper hat - you can utilize the buttons to run the speed-test maually and display the results to the screen.

To use the device you will need a few bits installted to your Raspberry Pi. You can see the full list below, but if you just want to get started, see the simple instruction below:

----------------------------------

sudo ./install.sh

You will also need to enable SPI in the raspi-config tool.

----------------------------------

If you want to go old-school and manually install all the bits and bobs, that fine, check out all the bits below.

sudo apt-get install python-pip python3-pip python-w1thermsensor python3-w1thermsensor python-spidev python3-spidev

sudo pip install gpiozero

sudo pip-3.2 install gpiozero

sudo pip install speedtest-cli

sudo pip install ipgetter

sudo pip3 install ipgetter

sudo pip install statistics

sudo pip3 install statistics

sudo pip install ascii_graph

sudo pip3 install ascii_graph

sudo apt-get install mpack zip ssmtp mailutils mpack

---------------------------------

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
