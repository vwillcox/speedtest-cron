#!/bin/sh

# Alton Waters Broadband Speed Checker
# Uses the speedtest.net servers and SpeedTest-CLI
# SpeedTest-cli by Matt Martz

# Version 1 - Simple Speed Testing

now="$(date +'%d/%m/%Y %H:%M')"
printf "Speed Test Ran at:  %s\n" "$now" >> /home/pi/speedtest/speedtest.txt
/usr/local/bin/speedtest-cli --simple >> /home/pi/speedtest/speedtest.txt 2>&1
echo  "----------" >> /home/pi/speedtest/speedtest.txt
