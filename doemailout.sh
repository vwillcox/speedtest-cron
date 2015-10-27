#!/bin/sh

# Network Testing Appliance
# Uses the speedtest.net servers and SpeedTest-CLI
# SpeedTest-cli by Matt Martz

# Version 1 - Simple Speed Testing
# Daily Email Script

filename=speedtest.txt
filedir=/home/pi/speedtest-cron/
current_time=$(date "+%Y.%m.%d-%H.%M.%S")
email_addresses="email@email.com email@email2.com"

mail -s "Speed Testing Results" $email_addresses < $filedir$filename
archive_name=$current_time.$filename
mv $filedir$filename $filedir$archive_name
