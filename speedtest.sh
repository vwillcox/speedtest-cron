#!/bin/sh

# Uses the speedtest.net servers and SpeedTest-CLI
# SpeedTest-cli by Matt Martz

# Version 1 - Simple Speed Testing

# Get the date 
now="$(date +'%d/%m/%Y %H:%M')"
# Print the date into the speedtest file.
printf "Speed Test Ran at:  %s\n" "$now" >> /home/pi/speedtest-cron/speedtest.txt
# Run a simple speedtest and pipe the results into the file
/usr/local/bin/speedtest-cli --simple >> /home/pi/speedtest-cron/speedtest.txt 2>&1
# Print a test delimiter into the file
echo  "----------" >> /home/pi/speedtest-cron/speedtest.txt

# Done and dusted. You have just run a speedtest.
# The results will be in a file called speedtest.txt
# Do what ever you need with this

