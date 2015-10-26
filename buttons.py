#!/usr/bin/python
###########################################################
#               Network Testing Appliance                 #
###########################################################
#             Originally by: Vincent Willcox              #
#                 http://talktech.info                    #
###########################################################
#                Version 1 - 25/10/2015                   #
###########################################################

from gpiozero import RGBLED, Button
import smbus
import time
import sys
import os
import subprocess
from PIL import Image
from PIL import ImageOps
import ImageDraw
import ImageFont
import ipgetter
import socket
import subprocess
import shlex
from EPD import EPD

led = RGBLED(red=6, green=12, blue=5)
button1 = Button(16)
button2 = Button(19)
button3 = Button(20)
button4 = Button(26)


if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
               pass
    return ip

def remove_rtc_module():
    exitCode = subprocess.call(["sudo", "rmmod", "rtc_ds3232"])
    if exitCode != 0:
        print ("Unable to remove RTC module, halting program");
        sys.exit()
    else:
        print ("RTC module removed");
        return;

def restore_rtc_module():
    exitCode = subprocess.call(["sudo", "modprobe", "rtc_ds3232"])
    if exitCode != 0:
        print ("Unable to restore RTC module, halting program")
        sys.exit()
    else:
        print ("RTC module restored");
        date = subprocess.check_output(["sudo", "hwclock", "-r"]);
        print (date);
        return;

def main():
    epd = EPD()
    try:
        while True:   # loop forever
		    # Check if the first button is pressed and reload the screen
            if button1.is_active:
                display_eedata(epd)
		    # Check if the second button is pressed and run a fresh speedtest, then reload the screen.
			# This will run over either the Ethernet or the wireless dongle if it is connected to a hot-spot.
            if button2.is_active:
                display_running(epd)
				# ToDo: Run this in pure python - for now another shell script is used
                subprocess.call(shlex.split('/home/pi/speedtest-cron/speedtest.sh'))
                display_eedata(epd)
    except KeyboardInterrupt:
      print ("Exiting Appliance Code")

# Code to simple refresh the screen
def display_eedata(epd):
    w = epd.width
    h = epd.height
    myip = ipgetter.myip()
    # Uncomment this line to display the true external IP
	#ext_ip = 'External: ' +  myip
	# Comment this line to remove the fake external IP
    ext_ip = 'External: 255.255.255.255'
    int_ip = get_lan_ip()
    int_ip = 'Internal: '  + int_ip
    #int_ip = int_ip.rstrip(5)
    f = open('/home/pi/speedtest-cron/speedtest.txt')
    lines = f.readlines()
    f.close()
    speedline1 = lines[-5].strip()
    speedline2 = lines[-4].strip()
    speedline3 = lines[-3].strip()
    speedline4 = lines[-2].strip()
    # initially set all white background
    image = Image.new('1', epd.size, WHITE)

    # prepare for drawing
    draw = ImageDraw.Draw(image)
    draw.rectangle((1, 1, w - 1, h - 1), fill=WHITE, outline=BLACK)
    draw.rectangle((2, 2, w - 2, h - 2), fill=WHITE, outline=BLACK)
    # text
    draw.text((5,5), speedline1, fill=BLACK, font=text_font1)
    draw.text((10,35), speedline2, fill=BLACK, font=text_font2)
    draw.text((10,65), speedline3, fill=BLACK, font=text_font2)
    draw.text((10,95), speedline4, fill=BLACK, font=text_font2)
    draw.text((10,125),  ext_ip, fill=BLACK, font=text_font2)
    draw.text((10,155),  int_ip, fill=BLACK, font=text_font2)
    # display image on the panel
    epd.display(image)
    epd.update()
	
# Code to show that a new speed test is running.
def display_running(epd):
    w = epd.width
    h = epd.height
    # initially set all white background
    image = Image.new('1', epd.size, WHITE)

    # prepare for drawing
    draw = ImageDraw.Draw(image)
    draw.rectangle((1, 1, w - 1, h - 1), fill=WHITE, outline=BLACK)
    draw.rectangle((2, 2, w - 2, h - 2), fill=WHITE, outline=BLACK)
    # text
    draw.text((10,35), 'Speed Test Running', fill=BLACK, font=text_font2)
    draw.text((10,65), 'Please Wait.......', fill=BLACK, font=text_font2)
    # display image on the panel
    epd.display(image)
    epd.update()


#main
if "__main__" == __name__:
    bus = smbus.SMBus(1)
    rtc = 0x68

    WHITE = 1
    BLACK = 0

    possible_fonts = [
        '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf',            # R.Pi
        '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf',   # R.Pi
        '/usr/share/fonts/truetype/freefont/FreeMono.ttf',                # R.Pi
    ]

    FONT_FILE = ''

    for f in possible_fonts:
        if os.path.exists(f):
            FONT_FILE = f
        break

    if '' == FONT_FILE:
        raise 'no font file found'

    TEXT_FONT_SIZE1 = 11
    TEXT_FONT_SIZE2 = 17
    text_font1 = ImageFont.truetype(FONT_FILE, TEXT_FONT_SIZE1)
    text_font2 = ImageFont.truetype(FONT_FILE, TEXT_FONT_SIZE2)
    main()
